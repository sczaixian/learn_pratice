import os
import uuid
import hashlib
# import environ
from django.template import loader
from django.conf import settings
from django.core.cache import cache, caches
from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives
from .login_proxy import login_blog, logout_blog
from django.contrib.sessions.models import Session
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage


PAGE_SIZE = 2
PAGE = 1

def check_request_type(request):
    if request.method == 'POST':
        return request.POST
    elif request.method == 'GET':
        return request.GET
    else:
        pass


def get_random_str():
    uuid_val = uuid.uuid4()
    uuid_str = str(uuid_val).encode('utf-8')
    md5 = hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()


def email_verify(request):
    content = check_request_type(request)
    email = content.get('email')
    random_str = get_random_str()
    url = 'http://192.168.37.128:8000/blog/active_email/' + random_str
    template = loader.get_template('active.html')
    html_str = template.render({'url':url})
    title = 'sss'
    msg = 'ddddd'
    from_email = settings.DEFAULT_FROM_EMAIL
    receiver = [
        email,
    ]
    send_mail(title, msg, from_email, receiver, html_message=html_str)
    cache.set(random_str, email, 120)  # ......
    return 'success'


def is_active(random_str):
    if not random_str or not random_str['random_str']:
        return False
    res = cache.get(random_str)
    if res:
        return True
    return False

# def test():
#     env = environ.Environ


# user_directory_path 函数必须接收 instace 和 filename 两个参数。
# 参数 instace 代表一个定义了 ImageField 的模型的实例，说白了就是当前数据记录；
# filename 是原本的文件名
def user_directory_path(instance, filename):
    user_id = instance.user_id
    photo_name = get_random_str()
    ext = filename.split('.').pop()
    sub_folder = 'file'
    if ext.lower() in ['jpg', 'gif', 'png', 'jpeg']:
        sub_folder = 'avatar'
    if ext.lower() in ['pdf', 'docx']:
        sub_folder = 'document'
    filename = '{0}/{1}.{2}'.format(sub_folder, photo_name, ext)
    # 系统路径分隔符差异，增强代码重用性
    return os.path.join(str(user_id), filename)


def login_tool(request, user):
    print('---------login_tool------------------')
    value = str(user.user_id) + get_random_str() + user.username
    print('value :  ', value)
    res = login_blog(request, user, value)
    print('-------res------')
    print('res :  ', res)


def logout_tool(request):
    print('--------logout_tool-------------')
    logout_blog(request)


def is_session_exists(session_key):
    print('------------is_session_exists--------------')
    check = Session.objects.filter(session_key__exact=session_key)
    print(check)
    print('session_key: ', session_key)
    print(caches[settings.SESSION_CACHE_ALIAS])
    print(session_key in caches[settings.SESSION_CACHE_ALIAS])
    print(session_key in caches[settings.SESSION_CACHE_ALIAS] or check)
    return session_key and (session_key in caches[settings.SESSION_CACHE_ALIAS] or check)


def paginator_tool(request, data_list):
    print('------------paginator_tool-----------------')
    content = check_request_type(request)
    print(content)
    page = PAGE
    if 'page' in content:
        page = content.get['page']
    page_size = PAGE_SIZE
    if 'page_size' in content:
        page = content.get['page_size']
    paginator = Paginator(data_list, page_size)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except InvalidPage:
        # 如果请求的页数不存在, 重定向页面
        return False
    except EmptyPage:
        # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
        articles = paginator.page(paginator.num_pages)
    return articles
