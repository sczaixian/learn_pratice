
import socket
import base64
import hashlib
from io import BytesIO

def socket_client():
    p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    p.connect(('127.0.0.1', 8080))
    while 1:
        msg = input('please input')
        # 防止输入空消息
        if not msg:
            continue
        p.send(msg.encode('utf-8'))  # 收发消息一定要二进制，记得编码
        if msg == '1':
            break
    p.close()


from threading import Lock
class Singleton(object):
    _instance_lock = Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, '_instance'):
            with Singleton._instance_lock:
                Singleton._instance = object.__new__(cls)

        return Singleton._instance


name = 'learn_pratice.apps.blog'
print(name.rpartition(".")[2])
print(name.rpartition("."))
# blog
# ('learn_pratice.apps', '.', 'blog')


def value_to_string(value):
    try:
        payload_file = BytesIO(value.encode('utf-8'))
        sha = hashlib.sha1()
        sha.update(payload_file.read())

        payload_file.seek(0)
        encoded_string = base64.b64encode(payload_file.read()).decode('utf-8')
        return encoded_string
    except IOError as e:
        return value


print(value_to_string('username'))
print(value_to_string('username'))
print(value_to_string('usssername'))

