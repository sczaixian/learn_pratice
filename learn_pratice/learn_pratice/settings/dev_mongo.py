from .common import *  # NOQA

INSTALLED_APPS.append('learn_pratice.apps.mongo_blog')

ROOT_URLCONF = 'learn_pratice.urls'

WSGI_APPLICATION = 'learn_pratice.wsgi.wsgi_blog_mongo.application'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace("\\", "/")

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
    'blog': {
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

DATABASE_ROUTERS = [
    'learn_pratice.settings.db_routers.AppsRouter',
]

DATABASE_APPS_MAPPING = {
    'blog': 'blog',
    'mongo_blog': 'mgo_db',
}


# qq POP3/SMTP 配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'black_weather_c@qq.com'
EMAIL_HOST_PASSWORD = 'qalkpyscgbrwbegd'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_USE_SSL = True

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

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
    },
    'redis': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
        }
    }
}

SESSION_CACHE_ALIAS = 'blog'