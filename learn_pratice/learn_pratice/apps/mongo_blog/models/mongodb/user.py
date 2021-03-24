
import re
from django.db import models
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils.functional import SimpleLazyObject
from learn_pratice.apps.mongo_blog.utils.tools import (user_directory_path, send_mail)


def _lazy_re_compile(regex, flags=0):
    """Lazily compile a regex with flags."""
    def _compile():
        # Compile the regex if it was not passed pre-compiled.
        if isinstance(regex, str):
            return re.compile(regex, flags)
        else:
            assert not flags, "flags must be empty if regex is passed pre-compiled"
            return regex
    return SimpleLazyObject(_compile)


@deconstructible
class RegexValidator:
    regex = ''
    message = _('Enter a valid value.')
    code = 'invalid'
    inverse_match = False
    flags = 0

    def __init__(self, regex=None, message=None, code=None, inverse_match=None, flags=None):
        if regex is not None:
            self.regex = regex
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
        if inverse_match is not None:
            self.inverse_match = inverse_match
        if flags is not None:
            self.flags = flags
        if self.flags and not isinstance(self.regex, str):
            raise TypeError("If the flags are set, regex must be a regular expression string.")

        self.regex = _lazy_re_compile(self.regex, self.flags)

    def __call__(self, value):
        """
        Validate that the input contains (or does *not* contain, if
        inverse_match is True) a match for the regular expression.
        """
        regex_matches = self.regex.search(str(value))
        invalid_input = regex_matches if self.inverse_match else not regex_matches
        if invalid_input:
            raise ValidationError(self.message, code=self.code)

    def __eq__(self, other):
        return (
            isinstance(other, RegexValidator) and
            self.regex.pattern == other.regex.pattern and
            self.regex.flags == other.regex.flags and
            (self.message == other.message) and
            (self.code == other.code) and
            (self.inverse_match == other.inverse_match)
        )


class UnicodeUsernameValidator(RegexValidator):
    regex = r'^[\w.@+-]+\Z'
    message = _(
        'Enter a valid username. This value may contain only letters, '
        'numbers, and @/./+/-/_ characters.'
    )
    flags = 0


class User(models.Model):

    username_validator = UnicodeUsernameValidator()

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    password = models.CharField(_('password'), max_length=128)
    nice_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='昵称')
    email = models.EmailField(_('email address'), blank=True)
    phone_num = models.IntegerField(default=0, verbose_name='手机号')
    identity_card = models.CharField(max_length=20, null=True, blank=True, verbose_name='身份证号')
    introduce = models.CharField(max_length=256, null=True, blank=True, verbose_name='自我描述')
    blog = models.OneToOneField(to='Blog', to_field='blog_id', null=True, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path, default='default.jpg', verbose_name='头像')
    is_active = models.BooleanField(_('active'), default=True)

    class Meta:
        app_label = 'mongo_blog'

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)