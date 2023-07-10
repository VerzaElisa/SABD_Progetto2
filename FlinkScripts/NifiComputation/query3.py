import json
import os
import time, datetime
from typing import Iterable
from pyflink.datastream.functions import ProcessWindowFunction, ReduceFunction
from Utility import OurTimestampAssigner, CountWindowProcessFunction, toString, csvToList ,CountWindowProcessFunctionPerc
from pyflink.common import SimpleStringSchema,WatermarkStrategy,Time ,Duration ,Row
from pyflink.common.watermark_strategy import TimestampAssigner
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer,KafkaSource,FlinkKafkaProducer
from pyflink.datastream.connectors.kafka import KafkaSink, KafkaRecordSerializationSchema,DeliveryGuarantee
from pyflink.datastream.window import WindowAssigner,TumblingEventTimeWindows,TumblingProcessingTimeWindows,GlobalWindows,TimeWindow
from pyflink.common.typeinfo import Types
from pyflink.datastream.time_characteristic import TimeCharacteristic
#libreria per il quantile dinamico
from psquare.psquare import PSquare
format = "%d-%m-%Y|%H:%M:%S.%f"

def my_map(obj):
    json_obj = json.loads(json.loads(obj))
    return json.dumps(json_obj["name"])
def toString(f):
    s=""
    for i in range(len(f)-1):
        s=s+str(f[i])+","
    s=s+str(f[len(f)-1])
    return s
def query3():
        env = StreamExecutionEnvironment.get_execution_environment()
        #env.set_stream_time_characteristic(TimeCharacteristic.EventTime)
        env.set_parallelism(1) 
        env.add_jars("file:///opt/flink-apps/flink-sql-connector-kafka-1.17.1.jar")
        env.add_python_file("file:///opt/flink-apps/Utility.py")
        #creazione della sorgente
        source = KafkaSource.builder() \
            .set_bootstrap_servers("kafka:29092") \
            .set_topics("user2") \
            .set_group_id("query3") \
            .set_value_only_deserializer(SimpleStringSchema()) \
            .build()
        #creazione del watermark per lo scorrimento del tempo in base agli aventi
        watermark=WatermarkStrategy\
              .for_monotonous_timestamps()\
              .with_timestamp_assigner(OurTimestampAssigner())
        #Creo i KafkaSink per andare a scrivere su 3 topic differenti i risultati delle query
        record_serializer1 = KafkaRecordSerializationSchema.builder() \
            .set_topic("resultQuery3-30minutes") \
            .set_value_serialization_schema(SimpleStringSchema()) \
            .build()
        sink1 = KafkaSink.builder() \
            .set_bootstrap_servers("kafka:29092") \
            .set_record_serializer(record_serializer1)\
            .build()
        record_serializer2 = KafkaRecordSerializationSchema.builder() \
            .set_topic("resultQuery3-1hour") \
            .set_value_serialization_schema(SimpleStringSchema()) \
            .build()
        sink2 = KafkaSink.builder() \
            .set_bootstrap_servers("kafka:29092") \
            .set_record_serializer(record_serializer2)\
            .build()
        record_serializer3 = KafkaRecordSerializationSchema.builder() \
            .set_topic("resultQuery3-1day") \
            .set_value_serialization_schema(SimpleStringSchema()) \
            .build()
        sink3 = KafkaSink.builder() \
            .set_bootstrap_servers("kafka:29092") \
            .set_record_serializer(record_serializer3)\
            .build()
        #inizio a creare il flusso dei dati comune
        ds=env.from_source(source,WatermarkStrategy.for_monotonous_timestamps(), "Kafka Source")\
                .map(func=csvToList)\
                .map(lambda f:f+[datetime.datetime.strptime(f[4]+'|'+f[3], format)])\
                .assign_timestamps_and_watermarks(watermark)\
                .key_by(key_selector=lambda f:f[0])

        ds1= ds.window(TumblingEventTimeWindows.of(Time.minutes(30)))\
                .process(CountWindowProcessFunctionPerc())\
                .key_by(lambda f:f[0].split(sep=".")[1])\
                .window(TumblingEventTimeWindows.of(Time.minutes(30)))\
                .reduce(ReduceFunctionPerc())\
                .map(lambda f:[f[2],f[0].split(sep=".")[1],f[7],f[8],f[9]])\
                .map(lambda f:toString(f),output_type=Types.STRING())\
                .sink_to(sink1)
        ds2= ds.window(TumblingEventTimeWindows.of(Time.hours(1)))\
                .process(CountWindowProcessFunctionPerc())\
                .key_by(lambda f:f[0].split(sep=".")[1])\
                .window(TumblingEventTimeWindows.of(Time.hours(1)))\
                .reduce(ReduceFunctionPerc())\
                .map(lambda f:[f[2],f[0].split(sep=".")[1],f[7],f[8],f[9]])\
                .map(lambda f:toString(f),output_type=Types.STRING())\
                .sink_to(sink2)
        ds3= ds.window(TumblingEventTimeWindows.of(Time.days(1)))\
                .process(CountWindowProcessFunctionPerc())\
                .key_by(lambda f:f[0].split(sep=".")[1])\
                .window(TumblingEventTimeWindows.of(Time.days(1)))\
                .reduce(ReduceFunctionPerc())\
                .map(lambda f:[f[2],f[0].split(sep=".")[1],f[7],f[8],f[9]])\
                .map(lambda f:toString(f),output_type=Types.STRING())\
                .sink_to(sink3)
        env.execute('query3')
        env.close()

class ReduceFunctionPerc(ReduceFunction):
    def reduce(self, a, b):
        a[3].update(b[1])
        a[4].update(b[1])
        a[5].update(b[1])
        count = a[6]
        if count < 5:
            count += 1
            return [a[0], a[1], a[2], a[3], a[4], a[5], count, '', '', '']
        count += 1
        return [a[0], a[1], a[2], a[3], a[4], a[5], count, a[3].p_estimate(), a[4].p_estimate(), a[5].p_estimate()]

if __name__ == '__main__':
    query3()