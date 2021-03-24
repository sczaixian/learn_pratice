import os
from django.db import models
from learn_pratice.apps.mongo_blog.utils.tools import user_directory_path


class Photo(models.Model):
    photo_id = models.AutoField(primary_key=True, verbose_name='相片ID')
    photo_name = models.CharField(max_length=100, verbose_name='相片名称')
    photo_src = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name='图片路径')
    user_id = models.IntegerField(verbose_name='所属用户ID')
    photo_sort = models.ForeignKey(to='PhotoSort', to_field='sort_img_id', on_delete=models.CASCADE)

    class Meta:
        app_label = 'mongo_blog'