import json
import os
import time, datetime
from typing import Iterable
from operator import itemgetter
from Utility import OurTimestampAssigner, CountWindowProcessFunction, Chart, csvToList, toString, MyMapperMeter


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

def query2():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)
    env.add_jars("file:///opt/flink-apps/flink-sql-connector-kafka-1.17.1.jar")
    env.add_jars("file:///opt/flink-apps/flink-metrics-prometheus_2.12-1.7.2.jar")
    env.add_python_file("file:///opt/flink-apps/Utility.py")
    env.get_config().set_latency_tracking_interval(200)

    source = KafkaSource.builder().set_bootstrap_servers("kafka:29092") \
                                  .set_topics("user") \
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

    
    ds=env.from_source(source, WatermarkStrategy.for_monotonous_timestamps(), "Kafka Source")\
          .map(func=csvToList)\
          .filter(func=lambda f:f[4]!="" and f[3]!="00:00:00.000")\
          .map(lambda f:f+[datetime.datetime.strptime(f[4]+'|'+f[3], format)])\
          .assign_timestamps_and_watermarks(watermark)\
          .key_by(key_selector=lambda f:f[0])
    ds1=  ds.window(TumblingEventTimeWindows.of(Time.minutes(30)))\
          .process(CountWindowProcessFunction())\
          .window_all(TumblingEventTimeWindows.of(Time.minutes(30)))\
          .process(Chart())\
          .map(lambda f:toString(f),output_type=Types.STRING())\
          .map(MyMapperMeter(), output_type=Types.STRING())\
          .sink_to(sink1)
    
    ds2=ds.window(TumblingEventTimeWindows.of(Time.hours(1)))\
        .process(CountWindowProcessFunction())\
        .window_all(TumblingEventTimeWindows.of(Time.hours(1)))\
        .process(Chart())\
        .map(lambda f:toString(f),output_type=Types.STRING())\
        .map(MyMapperMeter(), output_type=Types.STRING())\
        .sink_to(sink2)
    ds3=ds.window(TumblingEventTimeWindows.of(Time.days(1)))\
        .process(CountWindowProcessFunction())\
        .window_all(TumblingEventTimeWindows.of(Time.days(1)))\
        .process(Chart())\
        .map(lambda f:toString(f),output_type=Types.STRING())\
        .map(MyMapperMeter(), output_type=Types.STRING())\
        .sink_to(sink3)
    env.execute('query2')
    env.close()
    
if __name__ == '__main__':
    query2()