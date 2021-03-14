import redis


'''
redis-py提供两个类Redis和StrictRedis用于实现Redis的命令，
StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令，
Redis是StrictRedis的子类
'''
redis_host = '127.0.0.1'
redis_port = 6379
r = redis.Redis(host=redis_host, port=redis_port, db=0)
r.set('name', 'songjiang')
'''参数：
     set(name, value, ex=None, px=None, nx=False, xx=False)
     ex，过期时间（秒）
     px，过期时间（毫秒）
     nx，如果设置为True，则只有name不存在时，当前set操作才执行,同setnx(name, value)
     xx，如果设置为True，则只有name存在时，当前set操作才执行'''
# r.setex(name, value, time)  # 设置过期时间（秒）
# r.psetex(name, time_ms, value)  # 设置过期时间（豪秒）

# 批量设置值
# r.mset(name1='zhangsan', name2='lisi')
# r.mget({"name1":'zhangsan', "name2":'lisi'})

print(r.get('name'))

# 批量获取
# print(r.mget("name1", "name2"))
# li = ["name1", "name2"]
# print(r.mget(li))

# 设置新值，打印原值
# print(r.getset("name1", "wangwu")) #输出:zhangsan
# print(r.get("name1")) #输出:wangwu


# 根据字节获取子序列
# r.set("name", "zhangsan")
# print(r.getrange("name", 0, 3))#输出:zhan

# 修改字符串内容，从指定字符串索引开始向后替换，如果新值太长时，则向后添加
# r.set("name", "zhangsan")
# r.setrange("name", 1, "z")
# print(r.get("name")) # 输出:zzangsan
# r.setrange("name", 6, "zzzzzzz")
# print(r.get("name")) # 输出:zzangszzzzzzz

'''
redis-py使用connection pool来管理对一个redis server的所有连接，
避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。
可以直接建立一个连接池，然后作为参数Redis，
这样就可以实现多个Redis实例共享一个连接池
'''
pool = redis.ConnectionPool(host=redis_host, port=redis_port)
r2 = redis.Redis(connection_pool=pool)
r2.set('name', 'likui')
print(r2.get('name'))


















if __name__ == '__main__':
    pass