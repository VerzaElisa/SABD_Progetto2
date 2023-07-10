FROM docker.io/bitnami/spark:3
USER root
RUN pip install pandas
RUN pip install numpy
COPY metrics.properties /opt/bitnami/spark/conf/metrics.properties
COPY spark-defaults.conf /opt/bitnami/spark/conf/spark-defaults.conf
RUN echo "*.sink.jmx.class=org.apache.spark.metrics.sink.JmxSink" >> "$SPARK_HOME/conf/metrics.properties"
