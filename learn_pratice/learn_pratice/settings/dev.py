from .common import *  # NOQA




DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'myblog',
        'USER':'python',
        'PASSWORD':'sczaixian',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}

AUTH_USER_MODEL = 'blog.UserInfo'

EMAIL_HOST = ''
EMAIL_PORT = 465
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_USE_SSL = True

ABSOLOUTE_URL_OVERRIDES = {
    # 'blogs.weblog': lambda o : "/blogs/%s/" % o.slug,
}



# session存储的相关配置
# 数据库配置（默认）
# SESSION_ENGINE = 'django.contrib.sessions.backends.db' # 引擎（默认）
# SESSION_COOKIE_NAME ＝ "sessionid"   # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
# SESSION_COOKIE_PATH ＝ "/"    # Session的cookie保存的路径（默认）
# SESSION_COOKIE_DOMAIN = None    # Session的cookie保存的域名（默认）
# SESSION_COOKIE_SECURE = False    # 是否Https传输cookie（默认）
# SESSION_COOKIE_HTTPONLY = True    # 是否Session的cookie只支持http传输（默认）
# SESSION_COOKIE_AGE = 1209600    # Session的cookie失效日期（2周）（默认）
# SESSION_EXPIRE_AT_BROWSER_CLOSE = False   # 是否关闭浏览器使得Session过期（默认）
# SESSION_SAVE_EVERY_REQUEST = False   # 是否每次请求都保存Session，默认修改之后才保存（默认）
# 缓存配置
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # 引擎
# SESSION_CACHE_ALIAS = 'default'  # 使用的缓存别名（默认内存缓存，也可以是memcache），此处别名依赖缓存的设置
# SESSION_COOKIE_NAME ＝ "sessionid"  # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串
# SESSION_COOKIE_PATH ＝ "/"  # Session的cookie保存的路径
# SESSION_COOKIE_DOMAIN = None  # Session的cookie保存的域名
# SESSION_COOKIE_SECURE = False  # 是否Https传输cookie
# SESSION_COOKIE_HTTPONLY = True  # 是否Session的cookie只支持http传输
# SESSION_COOKIE_AGE = 1209600  # Session的cookie失效日期（2周）
# SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # 是否关闭浏览器使得Session过期
# SESSION_SAVE_EVERY_REQUEST = False  # 是否每次请求都保存Session，默认修改之后才保存
# 默认配置
# SESSION_ENGINE = 'django.contrib.sessions.backends.file' # 引擎
# SESSION_FILE_PATH = None     # 缓存文件路径，如果为None，则使用tempfile模块获取一个临时地址tempfile.gettempdir()
# SESSION_COOKIE_NAME ＝ "sessionid"    # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串
# SESSION_COOKIE_PATH ＝ "/"     # Session的cookie保存的路径
# SESSION_COOKIE_DOMAIN = None    # Session的cookie保存的域名
# SESSION_COOKIE_SECURE = False    # 是否Https传输cookie
# SESSION_COOKIE_HTTPONLY = True    # 是否Session的cookie只支持http传输
# SESSION_COOKIE_AGE = 1209600    # Session的cookie失效日期（2周）
# SESSION_EXPIRE_AT_BROWSER_CLOSE = False   # 是否关闭浏览器使得Session过期
# SESSION_SAVE_EVERY_REQUEST = False    # 是否每次请求都保存Session，默认修改之后才保存

#
# INSTALLED_APPS = [
#     # 图片上传模块 django-filer
#     'easy_thumbnails',
#     'filer',
#     'mptt',
# ]
#
# # 支持视网膜高分辨率设备
# THUMBNAIL_HIGH_RESOLUTION = True
#
# # 处理缩列图
# THUMBNAIL_PROCESSORS = (
#     'easy_thumbnails.processors.colorspace',
#     'easy_thumbnails.processors.autocrop',
#     'filer.thumbnail_processors.scale_and_crop_with_subject_location',
#     'easy_thumbnails.processors.filters',
# )
#
# # 存放图片文件夹设置
# FILER_STORAGES = {
#     'public': {
#         'main': {
#             'ENGINE': 'filer.storage.PublicFileSystemStorage',
#             'OPTIONS': {
#                 'location': '项目路径/media/filer',
#                 'base_url': '/media/filer/',
#             },
#             'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
#             'UPLOAD_TO_PREFIX': 'filer_public',
#         },
#         'thumbnails': {
#             'ENGINE': 'filer.storage.PublicFileSystemStorage',
#             'OPTIONS': {
#                 'location': '项目路径/media/filer_thumbnails',
#                 'base_url': '/media/filer_thumbnails/',
#             },
#         },
#     },
#     'private': {
#         'main': {
#             'ENGINE': 'filer.storage.PrivateFileSystemStorage',
#             'OPTIONS': {
#                 'location': '项目路径/smedia/filer',
#                 'base_url': '/smedia/filer/',
#             },
#             'UPLOAD_TO': 'filer.utils.generate_filename.randomized',
#             'UPLOAD_TO_PREFIX': 'filer_public',
#         },
#         'thumbnails': {
#             'ENGINE': 'filer.storage.PrivateFileSystemStorage',
#             'OPTIONS': {
#                 'location': '项目路径/smedia/filer_thumbnails',
#                 'base_url': '/smedia/filer_thumbnails/',
#             },
#         },
#     },
# }
#
