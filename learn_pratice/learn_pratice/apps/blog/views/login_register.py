# import re
# from django import forms
# from django.http import HttpResponseRedirect
# from django.contrib.auth import get_user_model
# from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from functools import wraps
from django.urls import reverse
from django.http import JsonResponse
from _datetime import datetime, timedelta
from django.shortcuts import render, redirect, HttpResponse
from learn_pratice.apps.blog.models.user_info import UserInfo
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.cache import cache_page
# from django.views.decorators.cache import cache_control
# from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from learn_pratice.apps.blog.utils.tools import check_request_type, \
                                                is_active, \
                                                email_verify, \
                                                login_tool, \
                                                logout_tool, \
                                                is_session_exists


# _RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
# _RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')


# @method_decorator(login_required)
# @method_decorator(csrf_protect)
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
    check = UserInfo.objects.filter(username__exact=username, password__exact=password)
    if check:
        print('--------------------check------------')
        print(check[0])
        # user = UserInfo.objects.using('blog').get(username=username)
        user = UserInfo.objects.get(username=username)
        result = {
            'username': username,
        }
        response = JsonResponse(result)
        print('---------1-------response--------------')
        print(response)     # <JsonResponse status_code=200, "application/json">
        print(response.content)

        # else:
        #     response.delete_cookie('username')
        # 手功完成 set_cookie
        # response.set_cookie('csrftoken', 'csrf-token-value')
        login_tool(request, user)
        print('----------------remember----------------')
        print(remember)
        if remember == 'off':
            request.session.set_expiry(0)
        else:
            response.set_cookie('username', username, expires=datetime.now() + timedelta(days=1))
        print('-----2---response-------------')
        print(response.content)
        return response
    msg = '账号或密码错误'
    return JsonResponse({'msg': msg})


def login_check(fun):
    print('---------longin_check-----------')
    @wraps(fun)
    def wrapper_fun(request, *args, **kwargs):
        print('-------------req----------------------')
        print(request)
        print(type(request.COOKIES))

        if {'username', 'sessionid'} <= set(request.COOKIES) and is_session_exists(request.COOKIES['sessionid']):
            return fun(request, *args, **kwargs)
        return render(request, 'login_register.html')
    return wrapper_fun


@login_check
@cache_page(6)  # 6 s
def index(request):

    # TODO: static_html
    print('---------index------------')
    username = request.COOKIES['username']
    check = UserInfo.objects.filter(username__exact=username)
    if check:
        # user = UserInfo.objects.using('blog').get(username=username)
        user = UserInfo.objects.get(username=username)
        return render(request, 'index.html', {'user': user})
    return render(request, 'login_register.html')


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
    # UserInfo.objects.using('blog').create(username=username, password=password, email=email)
    UserInfo.objects.create(username=username, password=password, email=email)
    return render(request, 'login_register.html')


def verify_email(request):
    return render(request, 'login_register.html', {'res': email_verify(request)})


def active_email(request, **kwargs):
    return render(request, 'login_register.html', {'res': is_active(kwargs)})


def logout(request):
    print('-------logout-----------------')
    print(request)
    if request.method == 'POST':
        print('post :  ', request.POST)
    else:
        print('get :  ', request.GET)
    logout_tool(request)
    response = redirect(reverse('blog:goto_register_page'))
    response.delete_cookie('username')
    return response


# django/util/cache
# @cache_control(max_age=360, must_revalidate=True, private=True)
# def private_cache(request):
#     pass