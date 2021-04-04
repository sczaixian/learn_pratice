
import json
from django.shortcuts import redirect
from django.core import serializers
from django.http import JsonResponse
from learn_pratice.apps.mongo_blog.models.mongodb.article import Article
from learn_pratice.apps.mongo_blog.utils.tools import paginator_tool, print


def add_article(request):
    print('------------add_article--------------------')
    if request.POST:
        content = request.POST
        article_name = content.get('title')
        user_id = content.get('user_id')
        article_click = 0
        article_content = content.get('content')

        print(content)

        Article.objects.create(
            article_name=article_name,
            user_id=int(user_id),
            article_click=article_click,
            article_content=article_content,
        )
    return redirect('blog:content')


def paginator_view(request):
    print('------------paginator_view-----------------')
    article_list = Article.objects.all()
    articles = paginator_tool(request, article_list)
    res = dict()
    if articles:
        res['articles'] = json.loads(serializers.serialize("json", articles))
    else:
        res['msg'] = 'vip666888'
    return JsonResponse(res)