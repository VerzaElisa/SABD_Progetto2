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
from pyflink.datastream.connectors.kafka import KafkaSink, KafkaRecordSerializationSchema,DeliveryGuarantee
from pyflink.datastream.connectors.file_system import FileSink, OutputFileConfig, RollingPolicy

from pyflink.datastream import StreamExecutionEnvironment, ProcessWindowFunction, ProcessFunction

format = "%d-%m-%Y|%H:%M:%S.%f"

def csvToList(f):
    x=f.split(sep=",")
    return x + [datetime.datetime.strptime(x[4]+'|'+x[3], format)]

def kafkaread():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)
    env.add_jars("file:///opt/flink-apps/flink-sql-connector-kafka-1.17.1.jar")
    
    source = KafkaSource.builder().set_bootstrap_servers("kafka:29092") \
                                  .set_topics("user2") \
                                  .set_group_id("query2") \
                                  .set_value_only_deserializer(SimpleStringSchema()) \
                                  .build()

    watermark=WatermarkStrategy.for_monotonous_timestamps()\
                               .with_timestamp_assigner(OurTimestampAssigner())
    #Creo i KafkaSink per andare a scrivere su 3 topic differenti i risultati delle query
    record_serializer1 = KafkaRecordSerializationSchema.builder() \
        .set_topic("resultQuery2-30minutes") \
        .set_value_serialization_schema(SimpleStringSchema()) \
        .build()
    sink1 = KafkaSink.builder() \
        .set_bootstrap_servers("kafka:29092") \
        .set_record_serializer(record_serializer1)\
        .build()
    record_serializer2 = KafkaRecordSerializationSchema.builder() \
        .set_topic("resultQuery2-1hour") \
        .set_value_serialization_schema(SimpleStringSchema()) \
        .build()
    sink2 = KafkaSink.builder() \
        .set_bootstrap_servers("kafka:29092") \
        .set_record_serializer(record_serializer2)\
        .build()
    record_serializer3 = KafkaRecordSerializationSchema.builder() \
        .set_topic("resultQuery2-1day") \
        .set_value_serialization_schema(SimpleStringSchema()) \
        .build()
    sink3 = KafkaSink.builder() \
        .set_bootstrap_servers("kafka:29092") \
        .set_record_serializer(record_serializer3)\
        .build()

    
    ds1=env.from_source(source, WatermarkStrategy.for_monotonous_timestamps(), "Kafka Source")\
          .map(func=csvToList)\
          .key_by(key_selector=lambda f:f[0])\
          .window(TumblingEventTimeWindows.of(Time.minutes(30)))\
          .process(CountWindowProcessFunction())\
          .window_all(TumblingEventTimeWindows.of(Time.minutes(30)))\
          .process(Chart())\
          .sink_to(sink1)
    ds2=env.from_source(source, WatermarkStrategy.for_monotonous_timestamps(), "Kafka Source")\
        .map(func=csvToList)\
        .key_by(key_selector=lambda f:f[0])\
        .window(TumblingEventTimeWindows.of(Time.hours(1)))\
        .process(CountWindowProcessFunction())\
        .window_all(TumblingEventTimeWindows.of(Time.hours(1)))\
        .process(Chart())\
        .sink_to(sink2)
    ds3=env.from_source(source, WatermarkStrategy.for_monotonous_timestamps(), "Kafka Source")\
        .map(func=csvToList)\
        .key_by(key_selector=lambda f:f[0])\
        .window(TumblingEventTimeWindows.of(Time.days(1)))\
        .process(CountWindowProcessFunction())\
        .window_all(TumblingEventTimeWindows.of(Time.days(1)))\
        .process(Chart())\
        .sink_to(sink3)

    env.execute('kafkaread')
    env.close()
    
if __name__ == '__main__':
    kafkaread()