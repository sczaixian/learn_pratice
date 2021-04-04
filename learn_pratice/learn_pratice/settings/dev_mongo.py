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
            'port': 27017,
            'username': 'm1',
            'password': '123',
            'authSource': 'my_mgodb',
            'authMechanism': 'SCRAM-SHA-1'
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



#
# #  log  首先创建日志存储路径.
# log_path = os.path.join(BASE_DIR, "logs")
# if not os.path.exists(log_path):
#     os.makedirs("logs")
# # DJANGO_LOG_LEVEL= DEBUG
# BASE_LOG_DIR = log_path
#
# LOGGING = {
#     'version': 1,  # 保留字
#     'disable_existing_loggers': False,  # 禁用已经存在的logger实例
#     # 日志文件的格式
#     'formatters': {
#         # 详细的日志格式
#         'standard': {
#             # 'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
#             #           '[%(levelname)s][%(message)s]'
#             'format': '[%(asctime)s][%(name)s][%(filename)s:%(lineno)d]'
#                       '[%(levelname)s][%(message)s]'
#         },
#         # 简单的日志格式
#         'simple': {
#             'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
#         },
#         # 定义一个特殊的日志格式
#         'collect': {
#             'format': '%(message)s'
#         }
#     },
#     # 过滤器
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     # 处理器
#     'handlers': {
#         'console': {  # 在终端打印
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],  # 只有在Django debug为True时才在屏幕打印日志
#             'class': 'logging.StreamHandler',  #
#             'formatter': 'simple'
#         },
#         'default': {  # 默认的
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
#             'filename': os.path.join(BASE_LOG_DIR, 'all.log'),  # 日志文件
#             'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
#             'backupCount': 3,  # 最多备份几个
#             'formatter': 'standard',
#             'encoding': 'utf-8',
#         },
#         'error': {  # 专门用来记错误日志
#             'level': 'ERROR',
#             'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
#             'filename': os.path.join(BASE_LOG_DIR, 'error.log'),  # 日志文件
#             'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
#             'backupCount': 5,
#             'formatter': 'standard',
#             'encoding': 'utf-8',
#         },
#         'collect': {  # 专门定义一个收集特定信息的日志
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
#             'filename': os.path.join(BASE_LOG_DIR, 'collect.log'),
#             'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
#             'backupCount': 5,
#             'formatter': 'collect',
#             'encoding': "utf-8"
#         },
#         # 'scprits_handler': {
#         #     'level': 'DEBUG',
#         #     'class': 'logging.handlers.RotatingFileHandler',
#         #     'filename': os.path.join(BASE_LOG_DIR, 'script.log'),
#         #     'maxBytes': 1024 * 1024 * 5,
#         #     'backupCount': 5,
#         #     'formatter': 'standard',
#         # }
#     },
#
#     'loggers': {
#         'django': {  # 默认的logger应用如下配置
#             'handlers': ['default', 'console', 'error'],  # 上线之后可以把'console'移除
#             'level': 'DEBUG',
#             'propagate': True,  # 向不向更高级别的logger传递
#         },
#         'collect': {  # 名为 'collect'的logger还单独处理
#             'handlers': ['console', 'collect'],
#             'level': 'INFO',
#         },
#         # 'scripts': {
#         #     'handlers': ['scprits_handler'],
#         #     'level': 'INFO',
#         #     'propagate': False
#         # },
#     },
# }

# 处理流程
#    formatter
# logger ----> handler ----------------> files, emails
#     filter

'''
此配置分成三个部分：

formatters: 指定输出的格式，被handler使用。

handlers： 指定输出到控制台还是文件中，以及输出的方式。被logger引用。

loggers： 指定django中的每个模块使用哪个handlers。以及日志输出的级别

注意：日志的输出级别是由loggers中的每个模块中level选项定义。如果没有配置，那么默认为warning级别

使用
import logging 
logger = logging.getLogger('django')
logger.info('-------------------------')
logger.error(str(e))
logger.warn('warn')
logger.debug('debug')  


参数：作用
 
%(levelno)s：打印日志级别的数值
%(levelname)s：打印日志级别的名称
%(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s：打印当前执行程序名
%(funcName)s：打印日志的当前函数
%(lineno)d：打印日志的当前行号
%(asctime)s：打印日志的时间
%(thread)d：打印线程ID
%(threadName)s：打印线程名称
%(process)d：打印进程ID

https://www.cnblogs.com/jackadam/p/9228116.html

'''