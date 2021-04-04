# -*- coding: utf-8 -*-

import sys
import json
import pandas as pd
import os
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError

KAFAKA_HOST = "localhost"  # 服务器端口地址
KAFAKA_PORT = 9092  # 端口号
KAFAKA_TOPIC = "test"  # topic

# data = pd.read_csv(os.getcwd() + '/data/abc.csv')
data = pd.read_csv(os.getcwd() + '/data/test.txt')
key_value = data.to_json()
print(key_value)


class MyKafkaProducer():
    '''
    生产模块：根据不同的key，区分消息
    '''

    def __init__(self, host, port, topic, key):
        self.host = host
        self.port = port
        self.topic = topic
        self.key = key
        self.producer = KafkaProducer(bootstrap_servers='{kafka_host}:{kafka_port}'.format(
            kafka_host=self.host,
            kafka_port=self.port)
        )

    def send_json_data(self, params):
        try:
            parmas_message = params  # 注意dumps
            producer = self.producer
            producer.send(self.topic, key=self.key, value=parmas_message.encode('utf-8'))
            producer.flush()
        except KafkaError as e:
            print(e)


class MyKafkaConsumer():

    def __init__(self, host, port, topic, group_id, key):
        self.host = host
        self.port = port
        self.topic = topic
        self.group_id = group_id
        self.key = key
        self.consumer = KafkaConsumer(self.topic, group_id=self.group_id,
                                      bootstrap_servers='{kafka_host}:{kafka_port}'.format(
                                          kafka_host=self.host,
                                          kafka_port=self.port)
                                      )

    def consume_data(self):
        try:
            for message in self.consumer:
                yield message
        except KeyboardInterrupt as e:
            print(e)


def sorted_dict_values(adict):
    items = adict.items()
    items = sorted(items, reverse=False)
    return [value for key, value in items]


def main(xtype, group, key):
    '''
    测试consumer和producer
    '''
    if xtype == "p":
        # 生产模块
        producer = MyKafkaProducer(KAFAKA_HOST, KAFAKA_PORT, KAFAKA_TOPIC, key)
        print("===========> producer:", producer)
        params = key_value
        producer.send_json_data(params)

    if xtype == 'c':
        # 消费模块
        consumer = MyKafkaConsumer(KAFAKA_HOST, KAFAKA_PORT, KAFAKA_TOPIC, group, key)
        print("===========> consumer:", consumer)

        message = consumer.consume_data()
        for msg in message:
            msg = msg.value.decode('utf-8')
            python_data = json.loads(msg)  ##这是一个字典
            key_list = list(python_data)
            test_data = pd.DataFrame()
            for index in key_list:
                print(index)
                if index == 'Month':
                    a1 = python_data[index]
                    data1 = sorted_dict_values(a1)
                    test_data[index] = data1
                else:
                    a2 = python_data[index]
                    data2 = sorted_dict_values(a2)
                    test_data[index] = data2
                    print(test_data)

            # print('value---------------->', python_data)
            # print('msg---------------->', msg)
            # print('key---------------->', msg.kry)
            # print('offset---------------->', msg.offset)


if __name__ == '__main__':
    main(xtype='p', group='py_test', key=None)
    main(xtype='c', group='py_test', key=None)