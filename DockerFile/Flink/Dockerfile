FROM flink:latest

# install python3 and pip3
RUN apt-get update -y && apt-get install -y python3 python3-pip python3-dev && rm -rf /var/lib/apt/lists/* && ln -s /usr/bin/python3 /usr/bin/python

# install PyFlink
COPY apache-flink*.tar.gz /
#COPY apache-flink-libraries-1.17.1.tar.gz /
RUN pip3 install /apache-flink-libraries*.tar.gz && pip3 install /apache-flink*.tar.gz
RUN pip install psquare