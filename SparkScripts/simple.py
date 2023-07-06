from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.streaming import StreamingContext
from pyspark import SparkContext
KAFKA_TOPIC_NAME = "user"
KAFKA_SINK_TOPIC = "sinkTopic"
KAFKA_BOOTSTRAP_SERVERS = "kafka:29092"
# CHECKPOINT_LOCATION = "LOCAL DIRECTORY LOCATION (FOR DEBUGGING PURPOSES)"
#CHECKPOINT_LOCATION = "/Users/aman.parmar/Documents/DATA_SCIENCE/KAFKA/CHECKPOINT"
sample_schema = (
        StructType()
        .add("id", StringType())
        .add("secType", StringType())
        .add("value", StringType())
        .add("hour", StringType())
        .add("date", StringType())
    )
if __name__ == "__main__":

    # STEP 1 : creating spark session object
    spark = (
        SparkSession.builder.appName("Kafka Pyspark Streamin Learning")
        .master("local[*]")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("ERROR")
    #ottengo uno streaming context
    ssc = StreamingContext(spark.sparkContext, batchDuration=1) #il batch duration può anche cambiare(?)
    # STEP 2 : reading a data stream from a kafka topic
    sampleDataframe = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS)
        .option("subscribe", KAFKA_TOPIC_NAME)
        .load()
    )
    base_df = sampleDataframe.selectExpr("CAST(value as STRING)")
    data_stream = ssc.queueStream([base_df.toPandas().values.tolist()])
    data_stream.pprint()
    ssc.start()
    ssc.awaitTermination()
    #tumblingWindows = base_df.withWatermark("timestamp", "30 minutes").groupBy("id", window("timestamp", "30 minutes")).count()
    data_stream.writeStream \
                   .format("console") \
                   .start()\
                   .awaitTermination()


    