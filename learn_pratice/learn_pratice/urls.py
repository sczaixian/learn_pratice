
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
# from learn_pratice.settings import dev
from django.urls import path, include, re_path
# from learn_pratice.apps.blog import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(('learn_pratice.apps.blog.urls', 'blog'))),
    path('blog_mongodb', include(('learn_pratice.apps.mongo_blog.urls', 'blog_mongodb'))),
    re_path(r'^medis/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
