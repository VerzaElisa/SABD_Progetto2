echo "Run Query1"
flink run --jobmanager localhost:8081 --python ./query1.py -r requirements.txt &
echo "Run Query2"
flink run --jobmanager localhost:8081 --python ./query2.py -r requirements.txt & 
echo "Run Query3"
flink run --jobmanager localhost:8081 --python ./query3.py -r requirements.txt &
