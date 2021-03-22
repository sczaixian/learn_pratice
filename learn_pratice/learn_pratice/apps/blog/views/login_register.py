# import re
# from django import forms
# from django.http import HttpResponseRedirect
# from django.contrib.auth import get_user_model
# from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.http import JsonResponse
from _datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from learn_pratice.apps.blog.models.mysql.user_info import UserInfo
# from django.views.decorators.cache import cache_control
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from learn_pratice.apps.blog.utils.tools import check_request_type, \
                                                is_active, \
                                                email_verify, \
                                                login_tool, \
                                                logout_tool


# _RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
# _RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')


# @method_decorator(login_required)
# @method_decorator(csrf_protect)
@require_http_methods(['POST'])
def login(request):
    print('------------login---------------------')
    content = check_request_type(request)
    username = content.get('username')
    password = content.get('password')
    try:
        remember = content.get('remember')
    except MultiValueDictKeyError as e:
        remember = False
    print('----------------content-----------------')
    print(content)
    check = UserInfo.objects.filter(username__exact=username, password__exact=password)
    if check:
        print('--------------------check------------')
        print(check[0])
        user = UserInfo.objects.get(username=username)
        response = JsonResponse({'user': username})
        # 手功完成 set_cookie
        # response.set_cookie('csrftoken', 'csrf-token-value')
        login_tool(request, user)
        print('----------------remember----------------')
        print(remember)
        if remember is 'false':
            request.session.set_expiry(0)
        response.set_cookie('user', username, expires=datetime.now() + timedelta(days=1))
        print('-----2---response-------------')
        print(response.content)
        return response
    msg = '账号或密码错误'
    return JsonResponse({'msg': msg})


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
    response = redirect(reverse('blog:register_page'))
    response.delete_cookie('username')
    return response


# django/util/cache
# @cache_control(max_age=360, must_revalidate=True, private=True)
# def private_cache(request):
#     pass