#! /bin/bash
name="apache-flink*.tar.gz"

docker compose down

cd ./DockerFile/Flink
ls -l $name > /dev/null
 
if [ "$?" -eq "0" ]
then
     echo "File già esistenti"
else
     echo "Download file"
     wget https://files.pythonhosted.org/packages/60/1e/ab18ee36565fdb4548a8466e3329087352be9d31a9b356a1f334c19e7369/apache-flink-1.17.1.tar.gz
     wget https://files.pythonhosted.org/packages/69/38/d9e594dc2dcc4f4e6091e851fbedc7c68f9de3391f72d94312f546a69a70/apache-flink-libraries-1.17.1.tar.gz
fi
docker build --tag pyflink:latest .
cd ../../FlinkScripts
wget https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-kafka/1.17.1/flink-sql-connector-kafka-1.17.1.jar
cd ..
docker compose build
docker compose up -d
docker exec -it flink apt-get update -y && apt-get install -y python3 python3-pip python3-dev && rm -rf /var/lib/apt/lists/* && ln -s /usr/bin/python3 /usr/bin/python
docker exec -it flink pip3 install /apache-flink-libraries*.tar.gz && pip3 install /apache-flink*.tar.gz
