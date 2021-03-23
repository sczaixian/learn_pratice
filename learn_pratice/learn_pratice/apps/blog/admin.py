
from django.contrib import admin
from learn_pratice.apps.blog.models.mysql.photo import Photo
from learn_pratice.apps.blog.models.mysql.blog import Blog
from learn_pratice.apps.blog.models.mysql.article import Article
from learn_pratice.apps.blog.models.mysql.article_sort import ArticleSort
from learn_pratice.apps.blog.models.mysql.photo_sort import PhotoSort
from learn_pratice.apps.blog.models.mysql.secret_message import SecretMessage
from learn_pratice.apps.blog.models.mysql.system_message import SystemMessage
from learn_pratice.apps.blog.models.mysql.user_info import UserInfo
from learn_pratice.apps.blog.models.mysql.user_attention import UserAttention
from learn_pratice.apps.blog.models.mysql.user_stay_message import UserStayMessage
#

admin.site.register(Photo)
admin.site.register(Blog)
admin.site.register(Article)
admin.site.register(ArticleSort)
admin.site.register(PhotoSort)
admin.site.register(SecretMessage)
admin.site.register(SystemMessage)
admin.site.register(UserInfo)
admin.site.register(UserAttention)
admin.site.register(UserStayMessage)
