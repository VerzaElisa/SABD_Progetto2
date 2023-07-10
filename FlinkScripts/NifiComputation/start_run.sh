echo "Run Query1"
flink run --detached --jobmanager localhost:8081 --python /opt/flink-apps/NifiComputation/query1.py -r requirements.txt 
echo "Run Query2"
flink run --detached --jobmanager localhost:8081 --python /opt/flink-apps/NifiComputation/query2.py -r requirements.txt 
echo "Run Query3"
flink run --detached --jobmanager localhost:8081 --python /opt/flink-apps/NifiComputation/query3.py -r requirements.txt 