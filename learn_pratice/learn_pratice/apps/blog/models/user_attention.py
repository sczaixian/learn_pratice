
from django.db import models


class UserAttention(models.Model):
    a_id = models.AutoField(primary_key=True, verbose_name='用户关注表')
    user = models.ForeignKey(to='UserInfo', to_field='u_id', on_delete=models.CASCADE, verbose_name='用户ID')
    attention_id = models.IntegerField(verbose_name='关注ID')

    class Meta:
        app_label = 'blog'