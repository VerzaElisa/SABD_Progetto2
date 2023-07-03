echo "Run Query1"
flink run --jobmanager localhost:8081 --jarfile flink-sql-connector-kafka-1.17.1.jar --python ./query1.py
#echo "Run Query2"
#flink run --jobmanager localhost:8081 --python ./query2.py
echo "Run Query3"
flink run --jobmanager localhost:8081 --jarfile flink-sql-connector-kafka-1.17.1.jar --python ./query3.py -r requirements.txt 
