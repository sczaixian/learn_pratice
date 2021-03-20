
from django.shortcuts import render, redirect


def init_blog(request):
    pass
    return render(request, 'index.html')


def init_content(request):
    print('------------init_content--------------')
    return render(request, 'content.html')


def add_article_page(request):
    print('------------add_blog----------------- ')
    pass
    return render(request, 'add_blog.html')


def goto_register_page(request):
    print('--------------goto_register_page-----------------')
    return render(request, 'login_register.html')