
import time
import json
from pymemcache.client.base import Client

'''
memcached是一款开源、高性能、分布式内存对象缓存系统，
可应用各种需要缓存的场景，
其主要目的是通过降低对Database的访问来加速web应用程序。
'''

data = {'iphone': ['iphone6', 'iphone7', 'iphone8'], 'Android': ['oppo', 'vivo']}
client = Client(('127.0.0.1', 1121))
key = 'Phone_menu'
# client.set(key, json.dumps(data))
print(client)


def get_data():
    """获取数据

    1.从mysql中获取
    2.从其他的一些接口获取数据
    """
    data = {'iphone': ['iphone6', 'iphone7', 'iphone8'], 'Android': ['oppo', 'vivo']}
    time.sleep(2)
    return data


def show_data(data):
    """显示数据内容
    """
    for k, v in data.items():
        print(f'{k} : {v}')


def set_memcache(k, data):
    '''将数据加入到缓存中
    '''
    try:
        client = Client(('127.0.0.1', 1121))
        client.set(k, json.dump(data))
        return True
    except Exception as e:
        print(e)
        return False


def get_memcached(k):
    '''获取memcached数据
    '''
    try:
        client = Client(('172.20.10.7', 11211))
        return json.load(client.get(k))
    except Exception as e:
        print(e)
        return False


def main():
    '''入口函数
    '''
    k = 'Phone_menu'
    get_memch = get_memcached(k)
    if get_memch:
        print('这是从缓存中取数据')
        show_data(get_data())
    else:
        print('这是从数据库取数据')
        data = get_data()
        show_data(data)
        set_memcache(k, data)

# main()
















