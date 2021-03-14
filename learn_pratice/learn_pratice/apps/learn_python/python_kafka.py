import pykafka
import names
from pykafka import KafkaClient
from kafka import KafkaProducer

'''
Kafka 是一种分布式的、分区的、多副本的基于发布／订阅的消息系统。
它是通过 zookeeper 进行协调，
常见可以用于 web/nginx 日志、访问日志、消息服务等。
主要应用场景为：日志收集系统和消息系统。
'''

# 创建连接到192.168.120.11:9092这个Broker的Producer,
# producer = KafkaProducer(bootstrap_server='192.168.120.11:9092')

# 循环向world这个Topic发送100个消息，消息内容都是some_message_bytes'，
# 这种发送方式不指定Partition，kafka会均匀大把这些消息分别写入5个Partiton里面
# for _ in range(3):
#     producer.send('world', b'some_message_bytes')



producer = KafkaProducer()
for _ in producer:
    name = names.get_full_name()
    future = producer.send('test', )






