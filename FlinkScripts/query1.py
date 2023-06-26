import json
import os
import time, datetime
from FlinkScripts.FirstElementTimestampAssigner import FirstElementTimestampAssigner

from pyflink.common import SimpleStringSchema,WatermarkStrategy,Time ,Duration
from pyflink.common.watermark_strategy import TimestampAssigner
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer,KafkaSource
from pyflink.datastream.window import WindowAssigner,TumblingEventTimeWindows,TumblingProcessingTimeWindows,GlobalWindows
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

    watermark=WatermarkStrategy\
              .for_bounded_out_of_orderness(Duration.of_seconds(10))\
              .with_timestamp_assigner(FirstElementTimestampAssigner())
    
    ds=env.from_source(source, WatermarkStrategy.for_monotonous_timestamps(), "Kafka Source")\
          .map(func=csvToList)\
          .filter(func=lambda f:f[0].endswith(".FR"))\
          .filter(func=lambda f:f[1]=='E')\
          .map(func=lambda f:(f[0]+"|"+f[4]+"|"+f[3].split(sep=":")[0],(1,float(f[2]))))\
          .key_by(key_selector=lambda f:f[0])
    ds1 = ds.window(TumblingProcessingTimeWindows.of(Time.seconds(30)))\
            .reduce(reduce_function=lambda a,b:(b[0],(a[1][0]+b[1][0],a[1][1]+b[1][1])))\
            .map(func=lambda f:(f[0],f[1][1]/f[1][0],f[1][0])).print()
    '''
    ds2 = ds.window(TumblingProcessingTimeWindows.of(Time.seconds(5)))\
            .reduce(reduce_function=lambda a,b:(b[0],(a[1][0]+b[1][0],a[1][1]+b[1][1])))\
            .map(func=lambda f:(f[0],f[1][1]/f[1][0],f[1][0])).print
    ds3 = ds.window(GlobalWindows.create())\
            .reduce(reduce_function=lambda a,b:(b[0],(a[1][0]+b[1][0],a[1][1]+b[1][1])))\
            .map(func=lambda f:(f[0],f[1][1]/f[1][0],f[1][0])).print()
    '''
    env.execute('kafkaread')

if __name__ == '__main__':
    kafkaread()