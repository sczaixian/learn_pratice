# _*_ coding: utf-8 _*_
from django.db import models
from learn_pratice.apps.blog.utils.tools import user_directory_path
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    # user_name = models.CharField(max_length=30, unique=True, verbose_name='')
    nice_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='昵称')
    phone_num = models.IntegerField(default=0, verbose_name='手机号')
    identity_card = models.CharField(max_length=20, null=True, blank=True, verbose_name='身份证号')
    user_discription = models.CharField(max_length=256, null=True, blank=True, verbose_name='自我描述')
    blog = models.OneToOneField(to='Blog', to_field='blog_id', null=True, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path, default='default.jpg', verbose_name='头像')
    first_name = None
    last_name = None
    user_permissions = None
    # is_staff = None
    # is_superuser = None
    # username = None

    class Meta:
        app_label = 'blog'
        db_table = 'blog_user'



    def __str__(self):
        return self.username


'''
MariaDB [myblog]> describe blog_user;
+------------------+--------------+------+-----+---------+----------------+
| Field            | Type         | Null | Key | Default | Extra          |
+------------------+--------------+------+-----+---------+----------------+
| password         | varchar(128) | NO   |     | NULL    |                |
| last_login       | datetime(6)  | YES  |     | NULL    |                |
| is_superuser     | tinyint(1)   | NO   |     | NULL    |                |
| username         | varchar(150) | NO   | UNI | NULL    |                |
| email            | varchar(254) | NO   |     | NULL    |                |
| is_staff         | tinyint(1)   | NO   |     | NULL    |                |
| is_active        | tinyint(1)   | NO   |     | NULL    |                |
| date_joined      | datetime(6)  | NO   |     | NULL    |                |
| user_id          | int(11)      | NO   | PRI | NULL    | auto_increment |
| nice_name        | varchar(30)  | YES  |     | NULL    |                |
| phone_num        | int(11)      | NO   |     | NULL    |                |
| identity_card    | varchar(20)  | NO   | UNI | NULL    |                |
| user_discription | varchar(256) | NO   |     | NULL    |                |
| photo            | varchar(100) | YES  |     | NULL    |                |
| blog_id          | int(11)      | YES  | UNI | NULL    |                |
+------------------+--------------+------+-----+---------+----------------+
'''
