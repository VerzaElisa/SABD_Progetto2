echo "Run Query1"
flink run --detached --jobmanager localhost:8081 --python /opt/flink-apps/query1.py -r requirements.txt 
echo "Run Query2"
flink run --detached --jobmanager localhost:8081 --python /opt/flink-apps/query2.py -r requirements.txt 
echo "Run Query3"
flink run --detached --jobmanager localhost:8081 --python /opt/flink-apps//query3.py -r requirements.txt 