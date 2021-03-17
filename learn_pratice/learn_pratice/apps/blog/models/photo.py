import os
from django.db import models

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


class Photo(models.Model):
    photo_id = models.AutoField(primary_key=True, verbose_name='相片ID')
    photo_name = models.CharField(max_length=100, verbose_name='相片名称')
    photo_src = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name='图片路径')
    user_id = models.IntegerField(verbose_name='所属用户ID')
    photo_sort = models.ForeignKey(to='PhotoSort', to_field='sort_img_id', on_delete=models.CASCADE)

    class Meta:
        app_label = 'blog'