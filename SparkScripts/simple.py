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
     
    df2= base_df.select(split(base_df.value,",")[0].alias("ID"),
                        split(base_df.value,",")[1].alias("SecType"),
                        split(base_df.value,",")[21].alias("Value").astype(FloatType()),
                        split(base_df.value,",")[23].alias("Ora"),
                        split(base_df.value,",")[26].alias("Data"),
                        )
    df3= df2.where(df2.Ora != "00:00:00.000")\
            .where(df2.Data!="")\
            .select(df2.ID,
                    df2.SecType,
                    df2.Value,
                    concat(concat(df2.Data,lit(" ")).alias("Data"),df2.Ora).alias("timestamp")
                    )
    df3 = df3.select(
                    df3.ID,
                    df3.SecType,
                    df3.Value,
                    to_timestamp(df3.timestamp,"dd-MM-yyyy HH:mm:ss.SSS").alias("my_timestamp")
                    )               
    tumblingWindows = df3.where(df3.SecType=="E")
                         .withWatermark("my_timestamp", "30 minutes").groupBy("ID", window("my_timestamp", "30 minutes")).
    tumblingWindows.writeStream \
                   .format("console") \
                   .start()\
                   .awaitTermination()


    