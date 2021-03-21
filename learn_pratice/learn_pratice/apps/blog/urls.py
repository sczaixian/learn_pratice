from django.urls import path, re_path
from learn_pratice.apps.blog.views import login_register as login_view, \
                                          content, \
                                          redirect
# from django.conf.urls import url

urlpatterns=[
    path('', login_view.index, name='index'),
    path('register/', login_view.register, name='register'),
    path('login/', login_view.login, name='login'),
    path('email_verify/', login_view.email_verify, name='pwd_email_verify'),
    path('active_email/<random_str>/', login_view.active_email, name='active_email'),
    path('logout/', login_view.logout, name='logout'),

    path('add_article/', content.add_article, name='add_article'),

    path('init_content/', redirect.init_content, name='content'),
    path('add_article_page/', redirect.add_article_page, name='add_article_page'),
    path('goto_register_page/', redirect.goto_register_page, name='goto_register_page'),
    path('init_blog/', redirect.init_blog, name='init_blog'),
]