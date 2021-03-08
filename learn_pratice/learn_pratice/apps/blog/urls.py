from django.urls import path
from learn_pratice.apps.blog.views import index

urlpatterns=[
    path('', index.index, name='index'),
]