
from django.db import models


class PhotoSort(models.Model):
    sort_img_id = models.AutoField(primary_key=True, verbose_name='相册ID')
    sort_img_name = models.CharField(max_length=20, verbose_name='相册名')
    user = models.ForeignKey(to='UserInfo', to_field='user_id', on_delete=models.CASCADE, verbose_name='所属用户ID')
    top_pic_src = models.IntegerField(verbose_name='封面图片ID')
    # sort_img_type = models.CharField(max_length=20, verbose_name='展示方式 \
    #                                                              0->仅主人可见, \
    #                                                              1->输入密码即可查看,2->仅好友能查看, \
    #                                                              3->回答问题即可查看')
    # img_password = models.CharField(max_length=32, verbose_name='查看密码')
    # img_sort_question = models.CharField(max_length=200, verbose_name='访问问题')
    # img_sort_answer = models.CharField(max_length=100, verbose_name='访问问题的答案')

    class Meta:
        app_label = 'blog'

