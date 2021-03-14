
import re
import socket


'''
替换1-20内的数字，3的倍数和5的倍数用不同的数字代替。
列出1到20的数字，
若是3的倍数就用apple代替，
若是5的倍数就用orange代替，
若既是3的倍数又是5的倍数就用appleorange代替。
'''
print(['apple'[i % 3 * len('apple'):]+'orange'[i % 5 * len('orange'):] or i for i in range(1, 21)])

'''
1：排序，按照名字A-Z排序
2：找出里面姓“ZHANG”的人数
3：找出名字里面最长的人代码思路
'''
names = (' Kunpen Ji, Li XIAO, Caron Li, Donl SHI, Ji ZHAO,Fia YUAN Y, Weue \
DING, Xiu XU, Haiying WANG, Hai LIN,Jey JIANG, Joson WANG E, Aiyang ZHANG,Hay \
MENG, Jak ZHANG E, Chang Zhang, Coro ZHANG')
names_sorted = sorted(list(map(lambda x: x.strip(), filter(lambda x: x.strip() != '', names.split(',')))))
print(names_sorted)

names_zhang = filter(lambda x: re.search('zhang', x, re.IGNORECASE), names_sorted)
print(list(names_zhang))

names_longest = sorted(names_sorted, key=lambda x: len(x), reverse=True)
print(names_longest[0])

'''
请用代码简答实现stack
'''


class Stack(object):
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            # raise Exception('empty')
            pass
        else:
            self.stack.pop()

    def push(self, value):
        self.stack.append(value)

    def is_empty(self):
        return not bool(self.stack)

    def top(self):
        if self.is_empty():
            # raise Exception('empty')
            pass
        else:
            return self.stack[-1]

    def clear(self):
        self.stack.clear()

    def size(self):
        return len(self.stack)





# redis如何实现主从复制？以及数据同步机制？

# 在Master和Slave互通之后，首先，Slave会发送sync同步指令，
# 当Master收到指令后，将在后台启动存盘进程，
# 同时收集所有来自Slave的修改数据集的指令信息，
# 当后台进程完成之后，Master将发送对应的数据库文件到对应的Slave中，
# 以完成一次完整的同步工作。
# 其次Slave在接受到数据库文件之后，将其存盘并加载到内存中。
# 最后，Master继续收集修改命令和新增的修改指令，并依次发送给Slave，
# 其将在本次执行这些数据的修改命令，从而最终达到数据同步的实现。


# 如何基于redis实现消息队列？

# Redis中五大数据结构之一—列表，其PUSH和POP命令遵循FIFO先进先出原则。
# 当我们需要发布消息的时候执行LPUSH(消息从左边进入队列)，
# 消息接收端执行RPOP获得消息(消息从右侧弹出)。对于列表，
# Redis提供了带有阻塞的命令(命令前加B)。因此，生产者lpush消息，
# 消费者brpop(从列表中弹出最右端元素，如无元素则一直阻塞到timeout)消息，
# 并设定超时时间timeout，可以减少redis的压力。
# 不要使用redis去做消息队列，这不是redis的设计目标。
# 但实在太多人使用redis去做去消息队列，redis的作者看不下去，
# 另外基于redis的核心代码，
# 另外实现了一个消息队列disque：https://github.com/antirez/disque












'''
socket
'''

# 明确配置变量
ip_port = ('127.0.0.1', 8080)
back_log = 5
buffer_size = 1024
# 创建一个TCP套接字
ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 套接字类型AF_INET, socket.SOCK_STREAM   tcp协议，基于流式的协议
ser.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 对socket的配置重用ip和端口号
# 绑定端口号
ser.bind(ip_port)  # 写哪个ip就要运行在哪台机器上
# 设置半连接池
ser.listen(back_log)  # 最多可以连接多少个客户端
while 1:
    # 阻塞等待，创建连接
    con, address = ser.accept()  # 在这个位置进行等待，监听端口号
    while 1:
        try:
            # 接受套接字的大小，怎么发就怎么收
            msg = con.recv(buffer_size)
            if msg.decode('utf-8') == '1':
                # 断开连接
                con.close()
            print('服务器收到消息', msg.decode('utf-8'))
        except Exception as e:
            break
# 关闭服务器
ser.close()





























