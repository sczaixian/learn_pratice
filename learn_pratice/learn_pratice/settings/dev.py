import os
from .common import *  # NOQA

INSTALLED_APPS.append('learn_pratice.apps.blog')

ROOT_URLCONF = 'learn_pratice.urls'

WSGI_APPLICATION = 'learn_pratice.wsgi.wsgi_blog.application'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace("\\", "/")


DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',
        'USER': 'python',
        'PASSWORD': 'sczaixian',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    },
    'mgo_db': {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': True,
        'NAME': 'myblog',
        'CLIENT': {
            'host': '127.0.0.1',
        }
    },
}

# DATABASE_ROUTERS = [
#     'learn_pratice.settings.db_routers.AppsRouter',
# ]
#
# DATABASE_APPS_MAPPING = {
#     'blog': 'blog',
#     'mongo_blog': 'mgo_db',
# }

AUTH_USER_MODEL = 'blog.UserInfo'

# qq POP3/SMTP 配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'black_weather_c@qq.com'
EMAIL_HOST_PASSWORD = 'qalkpyscgbrwbegd'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_USE_SSL = True

ABSOLOUTE_URL_OVERRIDES = {
    # 'blogs.weblog': lambda o : "/blogs/%s/" % o.slug,
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
# SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache_db'
# "django.contrib.sessions.cache"

# SESSION_ENGINE = 'django.contrib.sessions.backends.file'
# SESSION_FILE_PATH = '/blog_session/uid/'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'blog': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': [
            '127.0.0.1:11211',
            # 给缓存机器加权重
            # ('127.xxxxx:port', 5)
        ]
    },
    'file': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': 'cache/file',
        # 这里给出的是路径，但是更多时候是在项目根目录创建个文件夹，然后直接
        # os.path.join(BASE_DIR，‘cache/file’)
    },
    'python_redis': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "python_redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
        }
    }
}

SESSION_CACHE_ALIAS = 'blog'

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
