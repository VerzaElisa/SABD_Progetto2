import json
import os
import time, datetime
from FirstElementTimestampAssigner import FirstElementTimestampAssigner

from pyflink.common import SimpleStringSchema,WatermarkStrategy,Time ,Duration
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, Schema
from pyflink.table.expressions import col, UNBOUNDED_RANGE, CURRENT_RANGE
from pyflink.table.window import Over
from pyflink.datastream.connectors import KafkaSource
from pyflink.datastream.window import TumblingEventTimeWindows
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.window import TimeWindow
from pyflink.datastream.connectors import StreamingFileSink
from pyflink.datastream.functions import ReduceFunction, WindowFunction

format = "%d-%m-%Y|%H:%M:%S.%f"

def csvToList(f):
    x=f.split(sep=",")
    return x

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
                               .with_timestamp_assigner(FirstElementTimestampAssigner())
    
    ds=env.from_source(source, WatermarkStrategy.for_monotonous_timestamps(), "Kafka Source")\
          .map(func=csvToList)\
          .key_by(key_selector=lambda f:f[0])\
          .window(TumblingEventTimeWindows.of(Time.minutes(30)))
    
    #Alternativa a queste due righe, apply dove ogni riga diventa una tupla con nome data-ora, key by su questo campo, max e min su questo campo
    ds_min = ds.reduce(ReduceFunctionMin()).map(lambda f: (f[0], f[2]))
    ds_max = ds.reduce(ReduceFunctionMax()).map(lambda f: (f[0], f[2]))
    ds_all = ds_min.union(ds_max)\
                   .key_by(lambda x: x[0])\
                   .reduce(lambda a, b: (a[0], float(a[1]) - float(b[1])))\
                   .map(lambda f: (str(f[0]), float(f[1])), Types.TUPLE([Types.STRING(), Types.FLOAT()]))
    
    # interpret the insert-only DataStream as a Table
    t = t_env.from_data_stream(ds_all)
    t.print_schema()
    t_env.create_temporary_view("InputTable", t)
    res_table = t_env.sql_query("SELECT f0 f1 FROM (SELECT f0 f1, ROW_NUMBER() OVER (PARTITION BY f0 f1 ORDER BY f1 asc) AS rownum FROM InputTable)")

    # interpret the insert-only Table as a DataStream again
    res_ds = t_env.to_data_stream(res_table)

    # add a printing sink and execute in DataStream API
    res_ds.print()

    env.execute('kafkaread')


class ReduceFunctionMin(ReduceFunction):
    def reduce(self, a, b):
        time1 = datetime.datetime.strptime(a[4]+"|"+a[3], format)
        time1 = datetime.datetime.timestamp(time1)
        time2 = datetime.datetime.strptime(b[4]+"|"+b[3], format)
        time2 = datetime.datetime.timestamp(time2)
        if time1<time2:
            return a[0], a[1], a[2], a[3], a[4]
        else:
            return b[0], b[1], b[2], b[3], b[4]
        
class ReduceFunctionMax(ReduceFunction):
    def reduce(self, a, b):
        time1 = datetime.datetime.strptime(a[4]+"|"+a[3], format)
        time1 = datetime.datetime.timestamp(time1)
        time2 = datetime.datetime.strptime(b[4]+"|"+b[3], format)
        time2 = datetime.datetime.timestamp(time2)
        if time1>time2:
            return a[0], a[1], a[2], a[3], a[4]
        else:
            return b[0], b[1], b[2], b[3], b[4]

if __name__ == '__main__':
    kafkaread()