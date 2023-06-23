import json
import os

from pyflink.common import SimpleStringSchema,WatermarkStrategy, Time
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer,KafkaSource
from pyflink.datastream.window import WindowAssigner,TumblingEventTimeWindows
from pyflink.common.typeinfo import Types

def my_map(obj):
    json_obj = json.loads(json.loads(obj))
    return json.dumps(json_obj["name"])

def csvToList(f):
    x=f.split(sep=",")
    return x
def kafkaread():
    env = StreamExecutionEnvironment.get_execution_environment()
    
    env.add_jars("file:///opt/flink-apps/flink-sql-connector-kafka-1.17.1.jar")
    
    source = KafkaSource.builder() \
            .set_bootstrap_servers("kafka:29092") \
            .set_topics("user2") \
            .set_group_id("flink") \
            .set_value_only_deserializer(SimpleStringSchema()) \
            .build()
    ds=env.from_source(source, WatermarkStrategy.no_watermarks(), "Kafka Source")

    ds = ds.map(func=csvToList).filter(func=lambda f:f[0].endswith(".FR"))\
            .filter(func=lambda f:f[1]=='E')\
            .map(func=lambda f:(f[0]+"|"+f[4]+"|"+f[3].split(sep=":")[0],(1,float(f[2]))))\
            .key_by(key_selector=lambda f:f[0])\
            .reduce(func=lambda a,b:(b[0],(a[1][0]+b[1][0],a[1][1]+b[1][1])))\
            .map(func=lambda f:(f[0],f[1][1]/f[1][0],f[1][0]))
    ds.print()
    env.execute('kafkaread')

if __name__ == '__main__':
    kafkaread()