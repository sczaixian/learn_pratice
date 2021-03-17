
import os
from django.db import models
from django.contrib.auth.models import AbstractUser


def user_directory_path(instance, filename):
    ext = filename.split('.').pop()
    sub_folder = 'avatar'
    filename = '{0}.{1}{2}.{3}'.format(sub_folder, instance.username, instance.identity_card, ext)
    # 系统路径分隔符差异，增强代码重用性
    return os.path.join(instance.u_id, filename)


class UserInfo(AbstractUser):
    u_id = models.AutoField(primary_key=True)
    phone_num = models.IntegerField(default=0, verbose_name='手机号')
    identity_card = models.CharField(max_length=20, unique=True, verbose_name='身份证号')
    user_discription = models.CharField(max_length=256, verbose_name='自我描述')
    blog = models.OneToOneField(to='Blog', to_field='blog_id', null=True, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name='头像')

    class Meta:
        app_label = 'blog'


    def __str__(self):
        return self.username
