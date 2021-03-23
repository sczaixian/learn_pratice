

from django.db import models


class SecretMessage(models.Model):
    secret_id = models.AutoField(primary_key=True, verbose_name='用户私信表')
    # ???
    user = models.ForeignKey(to='UserInfo', to_field='user_id', on_delete=models.CASCADE, verbose_name='发信者ID')
    receive_id = models.IntegerField(verbose_name='收信者ID')
    message_topic = models.CharField(max_length=100, verbose_name='私信标题')
    message_content = models.TextField(max_length=255, verbose_name='私信内容')

    class Meta:
        app_label = 'mongo_blog'
