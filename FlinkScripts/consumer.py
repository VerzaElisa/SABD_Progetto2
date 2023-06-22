import json
import os

from pyflink.common import SimpleStringSchema
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer
from pyflink.common.typeinfo import Types


def my_map(obj):
    json_obj = json.loads(json.loads(obj))
    return json.dumps(json_obj["name"])


def kafkaread():
    env = StreamExecutionEnvironment.get_execution_environment()

    env.add_jars("file:///opt/flink-apps/flink-sql-connector-kafka-1.17.1.jar")

    deserialization_schema = SimpleStringSchema()

    kafkaSource = FlinkKafkaConsumer(
        topics='user-tracker',
        deserialization_schema=deserialization_schema,
        properties={'bootstrap.servers': 'kafka:9092', 'group.id': 'test'}
    )

    ds = env.add_source(kafkaSource).print()
    env.execute('kafkaread')
    print(ds)


if __name__ == '__main__':
    kafkaread()