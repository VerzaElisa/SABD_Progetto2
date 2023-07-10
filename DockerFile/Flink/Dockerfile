FROM flink:latest
# install python3 and pip3
#RUN apt-get update -y && apt-get install -y python3 python3-pip python3-dev && rm -rf /var/lib/apt/lists/* && ln -s /usr/bin/python3 /usr/bin/python
RUN echo "metrics.reporters: prom" >> "$FLINK_HOME/conf/flink-conf.yaml"
RUN echo "metrics.reporter.prom.factory.class: org.apache.flink.metrics.prometheus.PrometheusReporterFactory" >> "$FLINK_HOME/conf/flink-conf.yaml"
RUN echo "metrics.reporter.prom.port: 9999" >> "$FLINK_HOME/conf/flink-conf.yaml"