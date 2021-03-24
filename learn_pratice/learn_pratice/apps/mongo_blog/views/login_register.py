
from django.urls import reverse
from django.http import JsonResponse
from _datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from learn_pratice.apps.mongo_blog.models.mongodb.user import User
from django.views.decorators.http import require_http_methods
from learn_pratice.apps.mongo_blog.utils.tools import (
    check_request_type, is_active, email_verify, login_tool, logout_tool)


# _RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
# _RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')


@require_http_methods(['POST'])
def login(request):
    print('-----mongo_blog-------login---------------------')
    content = check_request_type(request)
    username = content.get('username')
    password = content.get('password')
    try:
        remember = content.get('remember')
    except MultiValueDictKeyError as e:
        remember = False
    print('----------------content-----------------')
    print(content)
    check = User.objects.filter(username__exact=username, password__exact=password)
    if check:
        print('--------------------check------------')
        print(check[0])
        user = User.objects.get(username=username)
        response = JsonResponse({'user': username})
        # login_tool(request, user)
        print('----------------remember----------------')
        print(remember)
        # if remember is 'false':
            # request.session.set_expiry(0)
        response.set_cookie('user', username, expires=datetime.now() + timedelta(days=1))
        print('-----2---response-------------')
        print(response.content)
        return response
    msg = '账号或密码错误'
    return JsonResponse({'msg': msg})


def register(request):
    print('----------mongo_blog-----register--------------')
    print(request.POST)
    content = check_request_type(request)
    username = content.get('username')
    password = content.get('password')
    email = content.get('email')
    User.objects.create(username=username, password=password, email=email)
    return render(request, 'login_register.html')


def verify_email(request):
    return render(request, 'login_register.html', {'res': email_verify(request)})


def active_email(request, **kwargs):
    return render(request, 'login_register.html', {'res': is_active(kwargs)})


def logout(request):
    print('-------logout------mongo_blog-----------')
    print(request)
    if request.method == 'POST':
        print('post :  ', request.POST)
    else:
        print('get :  ', request.GET)
    logout_tool(request)
    response = redirect(reverse('blog:register_page'))
    response.delete_cookie('username')
    return response
