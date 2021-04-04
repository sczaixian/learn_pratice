
from django.urls import path, include
from .views import (
    login_register as login_view, content, redirect, index)

from rest_framework import routers
from learn_pratice.apps.mongo_blog.views.drf import drf_view

router = routers.DefaultRouter()
router.register(r'users', drf_view.UserViewSet)


urlpatterns =[

    path('user_list/', drf_view.user_list, name='user_list'),
    path('rest_fw/', include(router.urls)),

    path('', index.index, name='index'),

    path('register/', login_view.register, name='register'),
    path('login/', login_view.login, name='login'),
    path('email_verify/', login_view.email_verify, name='pwd_email_verify'),
    path('active_email/<random_str>/', login_view.active_email, name='active_email'),
    path('logout/', login_view.logout, name='logout'),

    path('add_article/', content.add_article, name='add_article'),
    path('paginator_view/', content.paginator_view, name='paginator'),

    path('init_content_page/', redirect.init_content_page, name='content_page'),
    path('add_article_page/', redirect.add_article_page, name='add_article_page'),
    path('register_page/', redirect.register_page, name='register_page'),
    path('init_blog/', redirect.init_blog, name='init_blog'),
]