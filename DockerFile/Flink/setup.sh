apt-get update -y && apt-get install -y python3 python3-pip python3-dev && rm -rf /var/lib/apt/lists/* && ln -s /usr/bin/python3 /usr/bin/python
pip3 install /data/apache-flink-libraries*.tar.gz && pip3 install /data/apache-flink*.tar.gz
pip3 install psquare
cp  /opt/flink-apps/flink-metrics-prometheus_2.12-1.7.2.jar /opt/flink/lib