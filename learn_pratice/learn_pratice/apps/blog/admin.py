from django.contrib import admin
from .models.photo import Photo
from .models.blog import Blog
from .models.article import Article
from .models.article_sort import ArticleSort
from .models.photo_sort import PhotoSort
from .models.secret_message import SecretMessage
from .models.system_message import SystemMessage
from .models.user_info import UserInfo
from .models.user_attention import UserAttention
from .models.user_stay_message import UserStayMessage
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
