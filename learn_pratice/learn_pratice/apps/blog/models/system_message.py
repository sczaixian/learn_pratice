
from django.db import models


class SystemMessage(models.Model):
    system_id = models.AutoField(primary_key=True, verbose_name='系统通知')
    send_id = models.IntegerField(verbose_name='接受者ID')
    group_id = models.IntegerField(verbose_name='用户组ID')
    send_default = models.BooleanField(default=False, verbose_name='1时发送所有用户，0时则不采用')
    system_topic = models.CharField(max_length=100, verbose_name='通知内容')
    system_content = models.TextField(max_length=255, verbose_name='通知内容')

    class Meta:
        app_label = 'blog'