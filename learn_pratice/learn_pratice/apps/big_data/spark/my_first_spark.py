
from pyspark import SparkConf, SparkContext

# conf = SparkConf().setAppName('test').setMaster('local[*]')
# sc = SparkContext(conf=conf)

from pyspark.sql import SparkSession

session = SparkSession.builder.master('local[*]').appName('test').getOrCreate()

from pyspark.sql.types import *
import pyspark.sql.functions as f

df = session.read.csv(
    'abc.cvs',
    encoding='utf-8',
    header=False,
    schema=StructType([
        StructField('text', StringType()),
        StructField('index', StringType())
    ])
)

df.select(f.explode(f.split('text', ' ')).alias('word')).groupby('word').count().show()

'''
+----+-----+
|word|count|
+----+-----+
|   c|    1|
|   b|    1|
|   a|    1|
+----+-----+
'''

# from kafka.txt import conn
