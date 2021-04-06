
import json
import redis
import threading


class ListDAL:
    def __init__(self, host='localhost', port=6379, db=0, password=None, charset='UTF-8', expire=86400, max=10):
        self.host = host
        self.port = port
        self.db = db
        self.password = password
        self.charset = charset
        self.db = redis.StrictRedis(host, port, db, password, charset=charset, decode_responses=True)
        self.expire = expire  # 过期时间，默认86400(24小时)
        self.max = max  # 每个键允许存储的最大条数，默认10

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '{} {}'.format(__class__.__name__, self.__dict__)

    def __len__(self):
        '''库中键的数量'''
        return self.db.dbsize()

    @property
    def expire(self):
        return self._expire

    @expire.setter
    def expire(self, expire):
        if not isinstance(expire, int):
            raise TypeError
        self._expire = expire

    @property
    def max(self):
        return self._max

    @max.setter
    def max(self, max):
        if not isinstance(max, int):
            raise TypeError
        self._max = max

    def create(self, name, value):
        '''增，含新增和添加

        :param name: 键名
        :type name: str
        :param value: 可被json转换的任意值
        :return 是否成功
        :rtype: bool
        '''
        value_str = json.dumps(value, ensure_ascii=False)
        try:
            if self.db.llen(name) == 0:
                # 空的话右插并设置过期时间
                self.db.rpush(name, value_str)
            else:
                # 非空
                if self.db.llen(name) < self.max:
                    # 还能放
                    self.db.rpush(name, value_str)
                else:
                    # 放不下左弹再右插
                    self.db.lpop(name)
                    self.db.rpush(name, value_str)
            self.db.expire(name, self.expire)
        except Exception as e:
            print(str(e))
            return False
        return True

    def read(self, name, start=0, end=-1):
        '''查

        :param name: 键名
        :param start: 起点
        :param end: 终点
        :return: 指定范围的列表
        :rtype: list
        '''
        result = self.db.lrange(name, start, end)
        result = [json.loads(i) for i in result]
        return result

    def update(self, name, value, index=-1):
        '''改

        :param name: 键名
        :param value: 可被json转换的任意值
        :param index: 下标，默认修改最后一个
        :return 是否成功
        :rtype: bool
        '''
        value_str = json.dumps(value, ensure_ascii=False)
        try:
            result = self.db.lset(name, index, value_str)
        except Exception as e:
            print(str(e))
            return False
        return result

    def delete(self, name, num=1):
        '''删，优先删除旧数据

        :param name: 键名
        :param num: 条数
        :return: 删掉的内容
        :rtype: list or False
        '''
        if name == '*':
            # 防止SQL注入
            return False
        result = []
        if self.db.exists(name) == False:
            # 不存在该键
            return False
        exist_len = self.db.llen(name)  # 剩余条数
        num = min(num, exist_len, self.max)  # 能取的最大条数
        try:
            for i in range(num):
                value_str = self.db.lpop(name)  # 左弹
                value = json.loads(value_str)
                result.append(value)
        except Exception as e:
            print(str(e))
            return False
        return result

    def length(self, name):
        '''给定键查询长度

        :param name: 键名
        :return: 长度
        :rtype: int
        '''
        return self.db.llen(name)

    def get_names(self):
        '''所有键名'''
        return self.db.scan()[1]

    def empty(self):
        '''清空'''
        command = input(r'数据库共有{}条数据，确认清空请输入（确认）: '.format(len(self)))
        if command == '确认':
            if self.db.flushdb():
                print('清空成功')
        else:
            print('清空失败')

    def original_method(self, method, *args, **kwargs):
        pass
        # self.db.


class StringDAL:
    def __init__(self, host='localhost', port=6379, db=0, password=None, charset='UTF-8', expire=86400):
        self.host = host
        self.port = port
        self.db = db
        self.password = password
        self.charset = charset
        self.db = redis.StrictRedis(host, port, db, password, charset=charset, decode_responses=True)
        self.expire = expire  # 过期时间，默认86400(24小时)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '{} {}'.format(__class__.__name__, self.__dict__)

    def __len__(self):
        '''库中键的数量'''
        return self.db.dbsize()

    @property
    def expire(self):
        return self._expire

    @expire.setter
    def expire(self, expire):
        if not isinstance(expire, int):
            raise TypeError
        self._expire = expire

    def create(self, name, value):
        '''增，含新增和添加

        :param name: 键名
        :type name: str
        :param value: 可被json转换的任意值
        :return 是否成功
        :rtype: bool
        '''
        try:
            old = self.read(name)
            if old == None:
                old = value
            if isinstance(old, list):
                old.append(value)
            if isinstance(old, str):
                old = old + value
            if isinstance(old, tuple):
                old = old + value
            if isinstance(old, dict):
                old.update(value)
            if isinstance(old, set):
                old.add(value)
            value = old
            value_str = json.dumps(value, ensure_ascii=False)
            self.db.set(name, value_str, ex=self.expire)
        except Exception as e:
            print(str(e))
            return False
        return True

    def read(self, name):
        '''查

        :param name: 键名
        :return: json读取后的数据，键名不存在则返回None
        '''
        result = self.db.get(name)
        if result:
            result = json.loads(result)
        return result

    def update(self, name, value):
        '''改（覆盖）

        :param name: 键名
        :param value: 可被json转换的任意值
        :return 是否成功
        :rtype: bool
        '''
        try:
            value_str = json.dumps(value, ensure_ascii=False)
            result = self.db.set(name, value_str, ex=self.expire)
        except Exception as e:
            print(str(e))
            return False
        return result

    def delete(self, name):
        '''删

        :param name: 键名
        :return: 删掉的内容
        '''
        try:
            result = self.read(name)
            self.db.delete(name)
        except Exception as e:
            print(str(e))
            return False
        return result

    def length(self, name):
        '''给定键查询长度

        :param name: 键名
        :return: json读取后的数据长度
        :rtype: int
        '''
        return len(self.read(name))

    def get_names(self):
        '''所有键名'''
        return self.db.scan()[1]

    def empty(self):
        '''清空'''
        command = input(r'数据库共有{}条数据，确认清空请输入（确认）: '.format(len(self)))
        if command == '确认':
            if self.db.flushdb():
                print('清空成功')
        else:
            print('清空失败')


'''------------doc-------------------'''

    #
    # '''初始化'''
    # stringDAL = StringDAL()
    # print(stringDAL)
    #
    # '''设置过期时间和最大条数'''
    # stringDAL.expire = 10000  # 过期时间，单位s
    # print('过期时间: {}s'.format(stringDAL.expire))
    #
    # '''增'''
    # name = '小明'
    # value = {'语文': 70, '数学': 80, '英语': 90}
    # stringDAL.create(name, value)  # 新增
    # value = {'物理': 70, '化学': 80, '生物': 90}
    # stringDAL.create(name, value)  # 添加
    #
    # name = '小红'
    # value = {'语文': 80, '数学': 90, '英语': 100}
    # stringDAL.create(name, value)  # 新增
    #
    # names = stringDAL.get_names()
    # num = len(stringDAL)  # 数据库的键的数量
    # print('数据库共有{}个键，分别是: {}'.format(num, names))
    #
    # '''查'''
    # name = '小明'
    # num = stringDAL.length(name)  # 键的对应值的数量
    # print('小明的成绩共{}条，分别是: {}'.format(num, stringDAL.read(name)))
    #
    # '''改'''
    # name = '小明'
    # value = {'语文': 100, '数学': 100, '英语': 100}
    # stringDAL.update(name, value)  # 覆盖
    # print('小明的成绩修改后: {}'.format(stringDAL.read(name)))
    #
    # '''删'''
    # name = '小明'
    # result = stringDAL.delete(name)
    # print('小明的成绩删除结果: {}'.format(result))
    # print('小明的成绩删除后: {}'.format(stringDAL.read(name)))
    #
    # '''清空'''
    # stringDAL.empty()
    #
    # '''-------------------------------'''
    #
    # '''初始化'''
    # listDAL = ListDAL()
    # print(listDAL)
    #
    # '''设置过期时间和最大条数'''
    # listDAL.expire = 10000  # 过期时间，单位s
    # listDAL.max = 20  # 每个键允许存储的最大条数
    # print('过期时间: {}s'.format(listDAL.expire))
    # print('每个键存储的最大条数: {}'.format(listDAL.max))
    #
    # '''增'''
    # name = '小明'
    # value = {'语文': 70, '数学': 80, '英语': 90}
    # listDAL.create(name, value)  # 新增
    # value = {'物理': 70, '化学': 80, '生物': 90}
    # listDAL.create(name, value)  # 添加
    #
    # name = '小红'
    # value = {'语文': 80, '数学': 90, '英语': 100}
    # listDAL.create(name, value)  # 新增
    #
    # names = listDAL.get_names()
    # num = len(listDAL)  # 数据库的键的数量
    # print('数据库共有{}个键，分别是: {}'.format(num, names))
    #
    # '''查'''
    # name = '小明'
    # num = listDAL.length(name)  # 键的对应值的数量
    # print('小明的成绩共{}条，分别是: {}'.format(num, listDAL.read(name)))
    #
    # '''改'''
    # name = '小明'
    # value = {'语文': 100, '数学': 100, '英语': 100}
    # listDAL.update(name, value, index=0)
    # print('小明的成绩修改后: {}'.format(listDAL.read(name)))
    #
    # '''删'''
    # name = '小明'
    # num = 1
    # result = listDAL.delete(name, num)
    # print('小明的成绩删除{}条: {}'.format(num, result))
    # print('小明的成绩删除后: {}'.format(listDAL.read(name)))
    #
    # '''清空'''
    # listDAL.empty()