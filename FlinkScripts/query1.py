import json
import os
import time, datetime
from Utility import OurTimestampAssigner, toString ,queryADDTimestamp, csvToList
from pyflink.common import SimpleStringSchema,WatermarkStrategy,Time ,Duration ,Row
from pyflink.common.watermark_strategy import TimestampAssigner
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer,KafkaSource,FlinkKafkaProducer
from pyflink.datastream.connectors.kafka import KafkaSink, KafkaRecordSerializationSchema,DeliveryGuarantee
from pyflink.datastream.window import WindowAssigner,TumblingEventTimeWindows,TumblingProcessingTimeWindows,GlobalWindows
from pyflink.common.typeinfo import Types
from pyflink.datastream.time_characteristic import TimeCharacteristic

def my_map(obj):
    json_obj = json.loads(json.loads(obj))
    return json.dumps(json_obj["name"])

def query1():
        env = StreamExecutionEnvironment.get_execution_environment()
        #env.set_stream_time_characteristic(TimeCharacteristic.EventTime)
        env.set_parallelism(1) 
        env.add_jars("file:///opt/flink-apps/flink-sql-connector-kafka-1.17.1.jar")
        env.add_python_file("file:///opt/flink-apps/Utility.py")
        #creazione della sorgente
        source = KafkaSource.builder() \
            .set_bootstrap_servers("kafka:29092") \
            .set_topics("user") \
            .set_group_id("query1") \
            .set_value_only_deserializer(SimpleStringSchema()) \
            .build()
        #creazione del watermark per lo scorrimento del tempo in base agli aventi
        watermark=WatermarkStrategy\
              .for_monotonous_timestamps()\
              .with_timestamp_assigner(OurTimestampAssigner())
        #Creo i KafkaSink per andare a scrivere su 3 topic differenti i risultati delle query
        record_serializer1 = KafkaRecordSerializationSchema.builder() \
            .set_topic("resultQuery1-30minutes") \
            .set_value_serialization_schema(SimpleStringSchema()) \
            .build()
        sink1 = KafkaSink.builder() \
            .set_bootstrap_servers("kafka:29092") \
            .set_record_serializer(record_serializer1)\
            .build()
        record_serializer2 = KafkaRecordSerializationSchema.builder() \
            .set_topic("resultQuery1-1Days") \
            .set_value_serialization_schema(SimpleStringSchema()) \
            .build()
        sink2 = KafkaSink.builder() \
            .set_bootstrap_servers("kafka:29092") \
            .set_record_serializer(record_serializer2)\
            .build()
        record_serializer3 = KafkaRecordSerializationSchema.builder() \
            .set_topic("resultQuery1-Global") \
            .set_value_serialization_schema(SimpleStringSchema()) \
            .build()
        sink3 = KafkaSink.builder() \
            .set_bootstrap_servers("kafka:29092") \
            .set_record_serializer(record_serializer3)\
            .build()
        #inizio a creare il flusso dei dati comune
        ds=env.from_source(source,WatermarkStrategy.for_monotonous_timestamps(), "Kafka Source")\
            .map(func=csvToList)\
            .filter(func=lambda f:f[4]!="" and f[3]!="00:00:00.000")\
            .assign_timestamps_and_watermarks(watermark)\
            .filter(func=lambda f:f[0].endswith(".FR"))\
            .filter(func=lambda f:f[1]=='E')\
            .filter(func=lambda f:f[0].startswith("G"))\
            .map(func=lambda f:(f[0]+"|"+f[4]+"|"+f[3].split(sep=":")[0],(1,float(f[2]))))\
            .key_by(key_selector=lambda f:f[0])
        #separo per le tre finestre temporali
        ds1 = ds.window(TumblingEventTimeWindows.of(Time.minutes(30)))\
            .reduce(lambda a,b:(b[0],(a[1][0]+b[1][0],a[1][1]+b[1][1])),queryADDTimestamp())\
            .map(func=lambda f:toString([f[0]]+[f[1].split(sep="|")[0]]+[f[2][1]/f[2][0],f[2][0]]),output_type=Types.STRING())\
            .sink_to(sink1)
        ds2 = ds.window(TumblingEventTimeWindows.of(Time.days(1)))\
            .reduce(reduce_function=lambda a,b:(b[0],(a[1][0]+b[1][0],a[1][1]+b[1][1])))\
            .map(func=lambda f:toString(f[0].split(sep="|")+[f[1][1]/f[1][0],f[1][0]]),output_type=Types.STRING())\
            .sink_to(sink2)
        ds3 = ds.window(TumblingEventTimeWindows.of(Time.days(7)))\
            .reduce(reduce_function=lambda a,b:(b[0],(a[1][0]+b[1][0],a[1][1]+b[1][1])))\
            .map(func=lambda f:toString(f[0].split(sep="|")+[f[1][1]/f[1][0],f[1][0]]),output_type=Types.STRING())\
            .sink_to(sink3)

        env.execute('query1')
        env.close()

if __name__ == '__main__':
    query1()