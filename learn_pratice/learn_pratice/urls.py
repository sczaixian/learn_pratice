
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.urls import path, include, re_path




urlpatterns = [

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
    path('blog/', include(('learn_pratice.apps.blog.urls', 'blog'))),
    path('blog_mgodb/', include(('learn_pratice.apps.mongo_blog.urls', 'blog_mgodb'))),
    re_path(r'^medis/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
