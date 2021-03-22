

from django.db import models


class Article(models.Model):
    article_id = models.AutoField(primary_key=True, verbose_name='文章表')
    article_name = models.CharField(max_length=100, verbose_name='文章名称')
    article_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    article_click = models.IntegerField(default=0, verbose_name='查看人数')
    article_sort = models.ForeignKey(to='ArticleSort', blank=True, null=True, to_field='sort_article_id', on_delete=models.CASCADE, verbose_name='所属分类')
    user_id = models.IntegerField(verbose_name='所属用户')  #   username
    article_type = models.BooleanField(default=True, verbose_name='文章内容公开')
    article_content = models.TextField(verbose_name='文章内容')
    article_is_up = models.BooleanField(default=True, verbose_name='是否置顶')
    article_support = models.BooleanField(default=True, verbose_name='是否博主推荐')

    class Meta:
        app_label = 'blog'