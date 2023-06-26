from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.window import TumblingEventTimeWindows
from pyflink.common import Time, WatermarkStrategy
from pyflink.common.watermark_strategy import TimestampAssigner 
class FirstElementTimestampAssigner(TimestampAssigner):
    def extract_timestamp(self, value, record_timestamp):
        return value[2]
env = StreamExecutionEnvironment.get_execution_environment()

# Configurazione dell'ambiente di esecuzione
env.set_parallelism(1)  # Imposta il parallelismo a 1 per un esempio semplice

# Configurazione della sorgente dei dati con timestamp
data = [("apple", 1, 1624723200), ("banana", 1, 1624723201), ("apple", 1, 1624723202),
        ("banana", 1, 1624723203), ("apple", 1, 1624723204),("apple", 1, 1624723205),("apple", 1, 1624723214),
        ("apple", 1, 1624726204),("apple", 1, 1624726203    ),("banana", 1, 1624728204),("banana", 1, 1624729204)]

stream = env.from_collection(data)

# Definizione della strategia di watermark e assegnazione del timestamp
watermark_strategy = WatermarkStrategy.for_monotonous_timestamps() \
    .with_timestamp_assigner(FirstElementTimestampAssigner())

# Esecuzione del word count con finestre temporali
stream.assign_timestamps_and_watermarks(watermark_strategy) \
    .key_by(lambda f:f[0])\
    .window(TumblingEventTimeWindows.of(Time.seconds(1))) \
    .reduce(lambda a,b:(b[0],a[1]+b[1],b[2])) \
    .print()

# Avvio dell'esecuzione
env.execute("WordCount with TumblingEventTimeWindows")
