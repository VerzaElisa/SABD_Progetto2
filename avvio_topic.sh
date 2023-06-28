docker exec -it broker /bin/kafka-topics --create --topic user --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --create --topic user2 --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --create --topic resultQuery1-30minutes --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --create --topic resultQuery1-1Days --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --create --topic resultQuery1-Global --bootstrap-server localhost:9092