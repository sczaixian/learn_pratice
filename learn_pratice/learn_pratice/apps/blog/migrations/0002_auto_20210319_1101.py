# Generated by Django 3.1.7 on 2021-03-19 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_click',
            field=models.IntegerField(default=0, verbose_name='查看人数'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_sort',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.articlesort', verbose_name='所属分类'),
        ),
    ]
