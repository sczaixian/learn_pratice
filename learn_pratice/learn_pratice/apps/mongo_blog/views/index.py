
import json
from functools import wraps
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_http_methods
from learn_pratice.apps.mongo_blog.models.mongodb.article import Article
from learn_pratice.apps.mongo_blog.models.mongodb.user import User
from learn_pratice.apps.mongo_blog.utils.tools import (
    is_session_exists, paginator_tool, print)


def login_check(fun):
    print('-----mongo_blog----longin_check-----------')
    @wraps(fun)
    def wrapper_fun(request, *args, **kwargs):
        if {'user', 'sessionid'} <= set(request.COOKIES) and is_session_exists(request.COOKIES['sessionid']):
            return fun(request, *args, **kwargs)
        return render(request, 'login_register.html')
    return wrapper_fun


@cache_page(2)  # 15 minutes
@require_http_methods('GET')
@login_check
def index(request):
    print('-----mongo_blog----index------------')
    # TODO: static_html
    res = dict()
    article_list = Article.objects.all()
    articles = paginator_tool(request, article_list)
    res = dict()
    if articles:
        res['articles'] = articles
    else:
        res['msg'] = '000'
    print('---------articles--------------')
    # print(res['articles'])
    # print(res['articles'].number)
    # print(res['articles'].paginator.num_pages)
    username = request.COOKIES['user']
    check = User.objects.filter(username__exact=username)
    if check:
        print('--------check---------')
        user = User.objects.get(username=username)
        res['user'] = user
        print(res)
        return render(request, 'index.html', res)
    return render(request, 'login_register.html')


def paginator_view(request):
    print('-----------------------------')
    article_list = Article.objects.all()
    articles = paginator_tool(request, article_list)
    res = dict()
    if articles:
        res['articles'] = json.loads(serializers.serialize("json", articles))
    else:
        res['msg'] = 'vip666888'
    return JsonResponse(res)
