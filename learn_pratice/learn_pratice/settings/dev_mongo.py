import os
from .common import *  # NOQA

DEV_MONGO_APPS = [
    'learn_pratice.apps.mongo_blog',
    'rest_framework',
]
INSTALLED_APPS.extend(DEV_MONGO_APPS)


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

ROOT_URLCONF = 'learn_pratice.urls'

WSGI_APPLICATION = 'learn_pratice.wsgi.wsgi_blog_mongo.application'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace("\\", "/")

DATABASE_ROUTERS = [
    'learn_pratice.settings.db_routers.AppsRouter',
]

DATABASE_APPS_MAPPING = {
    'mongo_blog': 'mgo_db',
}

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'my_mgodb',
        # 'USER': 'python',
        # 'PASSWORD': 'sczaixian',
        # 'HOST': '127.0.0.1',
        # 'PORT': '3306',
    },
    'mgo_db': {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': True,
        'NAME': 'my_mgodb',
        'CLIENT': {
            'host': '127.0.0.1',
        }
    },
}

# qq POP3/SMTP 配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'black_weather_c@qq.com'
EMAIL_HOST_PASSWORD = 'qalkpyscgbrwbegd'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_USE_SSL = True
