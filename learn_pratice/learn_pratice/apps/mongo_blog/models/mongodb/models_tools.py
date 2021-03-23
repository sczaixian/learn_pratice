
'''
# # pip install pillow
# # pip install django-imagekit
# from imagekit.models import ImageSpecField
# from imagekit.processors import ResizeToFill
from django.contrib.auth.models import AbstractUser
import os
from django.db import models
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save

# user_directory_path 函数必须接收 instace 和 filename 两个参数。
# 参数 instace 代表一个定义了 ImageField 的模型的实例，说白了就是当前数据记录；
# filename 是原本的文件名
def user_directory_path(instance, filename):
    print('----------1--------')
    print(instance)
    print(filename)
    print('----------user_directory_path------------')
    ext = filename.split('.').pop()
    sub_folder = 'file'
    if ext.lower() in ['jpg', 'gif', 'png']:
        sub_folder = 'avatar'
    if ext.lower() in ['pdf', 'docx']:
        sub_folder = 'document'
    filename = '{0}.{1}{2}.{3}'.format(sub_folder, instance.username, instance.identity_card, ext)
    # 系统路径分隔符差异，增强代码重用性
    return os.path.join(instance.u_id, filename)


class UserInfo(AbstractUser):
    u_id = models.AutoField(primary_key=True)
    phone_num = models.IntegerField(default=0, verbose_name='手机号')
    identity_card = models.CharField(max_length=20, unique=True, verbose_name='身份证号')
    user_discription = models.CharField(max_length=256, verbose_name='自我描述')
    blog = models.OneToOneField(to='Blog', to_field='blog_id', null=True, on_delete=models.CASCADE)

    # upload_to 参数接收一个回调函数 user_directory_path，
    # 该函数返回具体的路径字符串，图片会自动上传到指定路径下，即 MEDIA_ROOT + upload_to
    photo = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name='头像')
    # photo_295_413 = ImageSpecField(  # 注意：ImageSpecField 不会生成数据库表的字段
    #     source='photo',
    #     processors=[ResizeToFill(295, 413)],  # 处理成一寸照片的大小
    #     format='JPEG',  # 处理后的图片格式
    #     options={'quality': 95}  # 处理后的图片质量
    # )

    # 默认情况下，imagekit 使用 imagekit.cachefiles.namers.source_name_as_path 来生成图片的路径
    # 上例定制后的图片会上传到 [MEDIA_ROOT]/CACHE/images/[upload_to]/[md5处理后的名字.jpg]
    # 想要自定义路径请参考 https://blog.csdn.net/weixin_42368421/article/details/84955946
    # def photo_295_413_url(self):
    #     if self.photo_295_413 and hasattr(self.photo_295_413, 'url'):
    #         return self.photo_295_413.url
    #     else:
    #         return '/media/default/user.jpg'

    # null 是针对数据库而言，如果 null = True, 表示数据库的该字段可以为空；
    # blank 是针对表单的，如果 blank = True，表示你的表单填写该字段的时候可以不填，但是对数据库来说，没有任何影响
    # photo = models.ImageField('照片', upload_to=user_directory_path, blank=True, null=True)

    # 这里定义一个方法，作用是当用户注册时没有上传照片，模板中调用 [ModelName].[ImageFieldName].url 时赋予一个默认路径
    # def photo_url(self):
    #     if self.photo and hasattr(self.photo, 'url'):
    #         return self.photo.url
    #     else:
    #         return '/media/default/user.jpg'

    # class Meta:
    #     复合主键(composit primary key)
    #     unique_together = ('u_id', 'name')

    def __str__(self):
        return self.username

#
# @receiver(post_save, sender=User)
# def create_user_extension(sender, instance, created, **kwargs):
#     if created:
#         UserInfo.objects.create(user=instance)
#     else:
#         instance.extension.save()

'''
