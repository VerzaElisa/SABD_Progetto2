import json
import os
import time, datetime
from typing import Iterable
from FirstElementTimestampAssigner import FirstElementTimestampAssigner
from operator import itemgetter
from Utility import OurTimestampAssigner, CountWindowProcessFunction, Chart


from pyflink.common import SimpleStringSchema,WatermarkStrategy,Time ,Duration
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, Schema
from pyflink.table.expressions import col, UNBOUNDED_RANGE, CURRENT_RANGE
from pyflink.table.window import Over
from pyflink.datastream.connectors import KafkaSource
from pyflink.datastream.window import TumblingEventTimeWindows
from pyflink.common.typeinfo import Types
from pyflink.datastream.window import TimeWindow
from pyflink.datastream.connectors import StreamingFileSink
from pyflink.datastream.functions import ReduceFunction
from pyflink.datastream.connectors.file_system import FileSink, OutputFileConfig, RollingPolicy

from pyflink.datastream import StreamExecutionEnvironment, ProcessWindowFunction, ProcessFunction

format = "%d-%m-%Y|%H:%M:%S.%f"

def csvToList(f):
    x=f.split(sep=",")
    return x + [datetime.datetime.strptime(x[4]+'|'+x[3], format)]

def kafkaread():
    env = StreamExecutionEnvironment.get_execution_environment()
    t_env = StreamTableEnvironment.create(env)

    env.set_parallelism(1)
    env.add_jars("file:///opt/flink-apps/flink-sql-connector-kafka-1.17.1.jar")
    
    source = KafkaSource.builder().set_bootstrap_servers("kafka:29092") \
                                  .set_topics("user2") \
                                  .set_group_id("query1") \
                                  .set_value_only_deserializer(SimpleStringSchema()) \
                                  .build()

    watermark=WatermarkStrategy.for_bounded_out_of_orderness(Duration.of_seconds(10))\
                               .with_timestamp_assigner(OurTimestampAssigner())
    
    ds=env.from_source(source, WatermarkStrategy.for_monotonous_timestamps(), "Kafka Source")\
          .map(func=csvToList)\
          .key_by(key_selector=lambda f:f[0])\
          .window(TumblingEventTimeWindows.of(Time.minutes(30)))\
          .process(CountWindowProcessFunction())\
          .window_all(TumblingEventTimeWindows.of(Time.minutes(30)))\
          .process(Chart()).print()


    env.execute('kafkaread')

if __name__ == '__main__':
    kafkaread()