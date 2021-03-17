
from django.db import models


class ArticleSort(models.Model):
    sort_article_id = models.IntegerField(auto_created=True, primary_key=True, unique=True, verbose_name='文章分类表')
    user_id = models.ForeignKey(to='UserInfo', to_field='u_id', on_delete=models.CASCADE, verbose_name='分类所属用户')
    sort_article_name = models.CharField(max_length=60, verbose_name='分类名称')

    class Meta:
        app_label = 'blog'
