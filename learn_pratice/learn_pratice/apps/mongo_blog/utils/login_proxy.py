
import base64
import string
import hashlib
import warnings
from io import BytesIO
from random import SystemRandom
from django.dispatch import Signal
from django.utils.deprecation import RemovedInDjango40Warning

user_logged_in = Signal()
# user_login_failed = Signal()
user_logged_out = Signal()

_sysrand = SystemRandom()
choice = _sysrand.choice

SESSION_KEY = '_blog_user_id'
CSRF_SECRET_LENGTH = 32
# CSRF_TOKEN_LENGTH = 2 * CSRF_SECRET_LENGTH
CSRF_ALLOWED_CHARS = string.ascii_letters + string.digits
# CSRF_SESSION_KEY = '_csrftoken'
NOT_PROVIDED = object()  # RemovedInDjango40Warning.


def login_blog(request, user, value):
    print('-----------login_custom_session----------------------')
    session_auth_hash = ''
    if user is None:
        user = request.user
    if hasattr(user, 'get_session_auth_hash'):
        session_auth_hash = user.get_session_auth_hash()

    if SESSION_KEY in request.session:
        pass
        # TODO:
        # if _get_user_session_key(request) != user.pk or (
        #         session_auth_hash and
        #         not constant_time_compare(request.session.get(HASH_SESSION_KEY, ''), session_auth_hash)):
        #     # To avoid reusing another user's session, create a new, empty
        #     # session if the existing session corresponds to a different
        #     # authenticated user.
        #     request.session.flush()
    else:
        request.session.cycle_key()
    request.session[SESSION_KEY] = value_to_string(value)
    if hasattr(request, 'user'):
        request.user = user
    rotate_token(request)
    user_logged_in.send(sender=user.__class__, request=request, user=user)
    return request


def get_random_string(length=NOT_PROVIDED, allowed_chars=(
    'abcdefghijklmnopqrstuvwxyz'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
)):

    if length is NOT_PROVIDED:
        warnings.warn(
            'Not providing a length argument is deprecated.',
            RemovedInDjango40Warning,
        )
        length = 12
    return ''.join(choice(allowed_chars) for i in range(length))


def _get_new_csrf_string():
    return get_random_string(CSRF_SECRET_LENGTH, allowed_chars=CSRF_ALLOWED_CHARS)


def _mask_cipher_secret(secret):
    mask = _get_new_csrf_string()
    chars = CSRF_ALLOWED_CHARS
    pairs = zip((chars.index(x) for x in secret), (chars.index(x) for x in mask))
    cipher = ''.join(chars[(x + y) % len(chars)] for x, y in pairs)
    return mask + cipher


def _get_new_csrf_token():
    return _mask_cipher_secret(_get_new_csrf_string())


def rotate_token(request):
    request.META.update({
        "CSRF_COOKIE_USED": True,
        "CSRF_COOKIE": _get_new_csrf_token(),
    })
    request.csrf_cookie_needs_reset = True


def value_to_string(value):
    try:
        payload_file = BytesIO(value.encode('utf-8'))
        sha = hashlib.sha1()
        sha.update(payload_file.read())
        payload_file.seek(0)
        encoded_string = base64.b64encode(payload_file.read()).decode('utf-8')
        return encoded_string
    except IOError as e:
        return value


def logout_blog(request):
    user = getattr(request, 'user', None)
    if not getattr(user, 'is_authenticated', True):
        user = None
    user_logged_out.send(sender=user.__class__, request=request, user=user)
    request.session.flush()
    if hasattr(request, 'user'):
        from django.contrib.auth.models import AnonymousUser
        request.user = AnonymousUser()