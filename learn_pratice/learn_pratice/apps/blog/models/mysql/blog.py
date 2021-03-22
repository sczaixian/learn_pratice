
from django.db import models


class Blog(models.Model):
    '''博客信息表'''
    blog_id = models.AutoField(primary_key=True, verbose_name='用户ID')
    blog_keyword = models.CharField(max_length=255, verbose_name='博客关键字')
    blog_description = models.CharField(max_length=255, verbose_name='博客描述')
    blog_name = models.CharField(max_length=36, verbose_name='博客名称')
    blog_title = models.CharField(max_length=128, verbose_name='博客标题')

    class Meta:
        app_label = 'blog'