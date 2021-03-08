from .common import *  # NOQA


DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'student2',
        'USER':'python',
        'PASSWORD':'sczaixian',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}

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