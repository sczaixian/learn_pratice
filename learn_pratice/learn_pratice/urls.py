
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
# from learn_pratice.settings import dev
from django.urls import path, include, re_path
# from learn_pratice.apps.blog import urls

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
    path('blog/', include(('learn_pratice.apps.blog.urls', 'blog'))),
    path('blog_mgodb/', include(('learn_pratice.apps.mongo_blog.urls', 'blog_mgodb'))),
    re_path(r'^medis/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
