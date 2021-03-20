from .common import *  # NOQA

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'blog': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',
        'USER': 'python',
        'PASSWORD': 'sczaixian',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

DATABASE_ROUTERS = [
    'learn_pratice.settings.db_routers.BlogRouter',
]

DATABASE_APPS_MAPPING = {
    'blog': 'blog',
}

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

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'blog': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

SESSION_CACHE_ALIAS = 'blog'
# SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_ENGINE = 'django.contrib.sessions.backends.cache_db'
# "django.contrib.sessions.cache"

# SESSION_ENGINE = 'django.contrib.sessions.backends.file'
# SESSION_FILE_PATH = '/blog_session/uid/'


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
