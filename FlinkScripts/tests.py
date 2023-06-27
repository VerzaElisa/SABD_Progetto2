from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.window import TumblingEventTimeWindows
from pyflink.common import Time, WatermarkStrategy,Types
from pyflink.common.watermark_strategy import TimestampAssigner 
from pyflink.datastream.connectors import FlinkKafkaConsumer,KafkaSource,FlinkKafkaProducer
from pyflink.datastream.connectors.kafka import KafkaSink, KafkaRecordSerializationSchema,DeliveryGuarantee

class FirstElementTimestampAssigner(TimestampAssigner):
    def extract_timestamp(self, value, record_timestamp):
        return value[2]
env = StreamExecutionEnvironment.get_execution_environment()

# Configurazione dell'ambiente di esecuzione
env.set_parallelism(1)  # Imposta il parallelismo a 1 per un esempio semplice
env.add_jars("file:///opt/flink-apps/flink-sql-connector-kafka-1.17.1.jar")
# Configurazione della sorgente dei dati con timestamp
data = [("apple","1"),("apple","1"),("banana","1"),("banana","1"),("apple","1"),("banana","1"),("banana","1"),("banana","1"),("apple","1")]

stream = env.from_collection(data)

# Definizione della strategia di watermark e assegnazione del timestamp
watermark_strategy = WatermarkStrategy.for_monotonous_timestamps() \
    .with_timestamp_assigner(FirstElementTimestampAssigner())

record_serializer = KafkaRecordSerializationSchema.builder() \
            .set_topic("result") \
            .set_value_serialization_schema(SimpleStringSchema()) \
            .build()
sink = KafkaSink.builder() \
            .set_bootstrap_servers("kafka:29092") \
            .set_record_serializer(record_serializer)\
            .build()
# Esecuzione del word count con finestre temporali
stream.map(lambda f:"("+str(f[0])+","+str(f[1])+")" , output_type=Types.STRING()).sink_to(sink)

# Avvio dell'esecuzione
env.execute("WordCount with TumblingEventTimeWindows")
