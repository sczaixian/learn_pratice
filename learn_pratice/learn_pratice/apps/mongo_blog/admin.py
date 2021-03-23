
from django.contrib import admin
#

from learn_pratice.apps.mongo_blog.models.mongodb.photo import Photo
from learn_pratice.apps.mongo_blog.models.mongodb.blog import Blog
from learn_pratice.apps.mongo_blog.models.mongodb.article import Article
from learn_pratice.apps.mongo_blog.models.mongodb.article_sort import ArticleSort
from learn_pratice.apps.mongo_blog.models.mongodb.photo_sort import PhotoSort
from learn_pratice.apps.mongo_blog.models.mongodb.secret_message import SecretMessage
from learn_pratice.apps.mongo_blog.models.mongodb.system_message import SystemMessage
from learn_pratice.apps.mongo_blog.models.mongodb.user_info import UserInfo
from learn_pratice.apps.mongo_blog.models.mongodb.user_attention import UserAttention
from learn_pratice.apps.mongo_blog.models.mongodb.user_stay_message import UserStayMessage


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
