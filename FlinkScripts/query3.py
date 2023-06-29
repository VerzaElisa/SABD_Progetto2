import json
import os
import time, datetime
from typing import Iterable
from pyflink.datastream.functions import ProcessWindowFunction 
from Utility import OurTimestampAssigner, CountWindowProcessFunction
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
class PercentileProcessFunction(ProcessWindowFunction):
    def process(self, key: str, context: ProcessWindowFunction.Context[TimeWindow], elements: Iterable[tuple]):
        percentile25 = PSquare(25)
        percentile50 = PSquare(50)
        percentile75 = PSquare(75)
        for e in elements:
            percentile25.update(e[1])
            percentile50.update(e[1])
            percentile75.update(e[1])
        return [[key,percentile25.p_estimate(),percentile50.p_estimate(),percentile75.p_estimate()]]
 
def my_map(obj):
    json_obj = json.loads(json.loads(obj))
    return json.dumps(json_obj["name"])

def csvToList(f):
    x=f.split(sep=",")
    return x
def toString(f):
    s=""
    for i in range(len(f)-1):
        s=s+str(f[i])+","
    s=s+str(f[len(f)-1])
    return s
def Quantile(x):
    n=n+1

def kafkaread():
        env = StreamExecutionEnvironment.get_execution_environment()
        #env.set_stream_time_characteristic(TimeCharacteristic.EventTime)
        env.set_parallelism(1) 
        env.add_jars("file:///opt/flink-apps/flink-sql-connector-kafka-1.17.1.jar")
        #creazione della sorgente
        source = KafkaSource.builder() \
            .set_bootstrap_servers("kafka:29092") \
            .set_topics("user2") \
            .set_group_id("flink") \
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
        #inizio a creare il flusso dei dati comune
        ds=env.from_source(source,WatermarkStrategy.for_monotonous_timestamps(), "Kafka Source")\
            .map(func=csvToList)\
            .assign_timestamps_and_watermarks(watermark)\
            .key_by(key_selector=lambda f:f[0])\
            .window(TumblingEventTimeWindows.of(Time.minutes(30)))\
            .process(CountWindowProcessFunction())\
            .key_by(lambda f:f[0].split(sep=".")[1])\
            .window(TumblingEventTimeWindows.of(Time.minutes(30)))\
            .process(PercentileProcessFunction())\
            .print()
        env.execute('kafkaread')
        env.close()

if __name__ == '__main__':
    kafkaread()