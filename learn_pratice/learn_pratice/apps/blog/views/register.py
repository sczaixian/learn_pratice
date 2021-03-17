import re
from django.http import HttpResponse
from django.shortcuts import render

_RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')







# pip install django-filer


def register(request):
    photo = request.FILES.get('photo')
    return HttpResponse('register!!')