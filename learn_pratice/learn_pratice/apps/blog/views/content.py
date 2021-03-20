from django.shortcuts import render, redirect
from learn_pratice.apps.blog.models.article import Article


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