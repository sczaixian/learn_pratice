import re
from learn_pratice.apps.blog.models.user_info import UserInfo
from _datetime import datetime, timedelta
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import get_user_model
from learn_pratice.apps.blog.utils.tools import check_request_type, \
                                                is_active, \
                                                email_verify, \
                                                login_tool
from django import forms
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from functools import wraps
from django.utils.datastructures import MultiValueDictKeyError

# _RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
# _RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')


def login_check(fun):
    print('---------longin_check-----------')
    @wraps(fun)
    def wrapper_fun(request, *args, **kwargs):
        if 'username' in request.COOKIES and 'pwd' in request.COOKIES:
            print('----inner-----')
            return fun(request, *args, **kwargs)
        # TODO:

        print('------not_cookies------')
        return render(request, 'login_register.html')
    return wrapper_fun


# @method_decorator(ensure_csrf_cookie)
def login(request):
    print('------------login---------------------')
    content = check_request_type(request)
    username = content.get('username')
    password = content.get('password')
    try:
        remember = content.get('remember')
    except MultiValueDictKeyError as e:
        remember = 'off'
    print('----------------content-----------------')
    print(content)
    check = UserInfo.objects.using('blog').filter(username__exact=username, password__exact=password)
    if check:
        print('--------------------check------------')
        print(check[0])
        user = UserInfo.objects.using('blog').get(username=username)
        result = {
            'username': username,
        }
        response = JsonResponse(result)
        print('----------------response--------------')
        print(response)     # <JsonResponse status_code=200, "application/json">
        print(response.content)
        if remember == 'on':
            response.set_cookie('username', username, expires=datetime.now() + timedelta(days=1))
            # response.set_cookie('pwd', password, expires=datetime.now() + timedelta(days=1))
        # 手功完成 set_cookie
        # response.set_cookie('csrftoken', 'csrf-token-value')
        login_tool(request, user)
        return response
    msg = '账号或密码错误'
    return JsonResponse({'msg': msg})


@login_check
def index(request):
    print('---------index------------')
    username = request.COOKIES['username']
    password = request.COOKIES['pwd']
    check = UserInfo.objects.using('blog').filter(username__exact=username, password__exact=password)
    if check:
        user = UserInfo.objects.using('blog').get(username=username)
        return render(request, 'index.html', {'user': user})
    return render(request, 'index.html')


def register(request):
    # 这个方法会从settings中找AUTH_USER_MODEL ,然后取得的User
    # 至于为何不直接那models里的User  暂时不清楚,后续会去测试,知道后再修改本文
    # user = get_user_model()
    print('---------------register--------------')
    print(request.POST)
    content = check_request_type(request)
    username = content.get('username')
    password = content.get('password')
    email = content.get('email')
    UserInfo.objects.using('blog').create(username=username, password=password, email=email)
    return render(request, 'login_register.html')


def verify_email(request):
    return render(request, 'login_register.html', {'res': email_verify(request)})


def active_email(request, **kwargs):
    return render(request, 'login_register.html', {'res': is_active(kwargs)})


def logout(request):
    response = HttpResponse()
    response.delete_cookie('username')
    request.session.flush()
    return render(request, 'login_register.html')