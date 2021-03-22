

from django.db import models


class UserStayMessage(models.Model):
    stay_id = models.AutoField(primary_key=True, verbose_name='留言表')
    user_id = models.IntegerField(verbose_name='用户ID')
    stay_user_id = models.IntegerField(verbose_name='留言者ID')
    message_content = models.TextField(max_length=255, verbose_name='留言内容')
    message_stay_time = models.DateTimeField(auto_now_add=True, verbose_name='留言时间')

    class Meta:
        app_label = 'blog'