
from django.shortcuts import render, redirect
from learn_pratice.apps.mongo_blog.utils.tools import (print)


def init_blog(request):
    pass
    return render(request, 'index.html')


def init_content_page(request):
    print('------------init_content--------------')
    return render(request, 'content.html')


def add_article_page(request):
    print('------------add_blog----------------- ')
    pass
    return render(request, 'add_blog.html')


def register_page(request):
    print('--------------register_page-----------------')
    return render(request, 'login_register.html')