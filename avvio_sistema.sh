#! /bin/bash
name="apache-flink*.tar.gz"
nameSql="flink-sql-connector-kafka-1.17.1.jar"
dataset="out600_combined+header.csv"
docker compose down

ls -l $dataset > /dev/null
if [ "$?" -eq "0" ]
then
     echo "File già esistenti"
else
     echo "Download Dataset"
     wget http://www.ce.uniroma2.it/courses/sabd2223/project/out600_combined+header.csv
fi

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
ls -l $nameSql > /dev/null
 
if [ "$?" -eq "0" ]
then
     echo "File già esistente"
else
     echo "Download file sql"
     wget https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-kafka/1.17.1/flink-sql-connector-kafka-1.17.1.jar
fi
cd ..
cd ./DockerFile/SparkBITNAMI/
docker build -t kobspark .
cd ../..
docker compose build
docker compose up -d
echo "inizio setup Flink"
docker exec -it flink sh /data/setup.sh
docker exec -it flink_worker1 sh /data/setup.sh
docker exec -it flink_worker2 sh /data/setup.sh
docker exec -it flink_worker3 sh /data/setup.sh

echo "inizio setup Kafka Topic"
bash avvio_topic.sh

echo "inizio setup NIFI"
cd ScriptSetUpNIFI
bash LogIn.sh
cd ..