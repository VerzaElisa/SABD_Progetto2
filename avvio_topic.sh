echo "Cancello i topic"
docker exec -it broker /bin/kafka-topics --delete --if-exists --topic user --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --delete --if-exists --topic user2 --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --delete --if-exists --topic resultQuery1-30minutes --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --delete --if-exists --topic resultQuery1-1Days --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --delete --if-exists --topic resultQuery1-Global --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --delete --if-exists --topic resultQuery2-30minutes --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --delete --if-exists --topic resultQuery2-1hour --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --delete --if-exists --topic resultQuery2-1day --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --delete --if-exists --topic resultQuery3-30minutes --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --delete --if-exists --topic resultQuery3-1hour --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --delete --if-exists --topic resultQuery3-1day --bootstrap-server localhost:9092
echo "Creo i topic"
docker exec -it broker /bin/kafka-topics --create --topic user --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --create --topic user2 --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --create --topic resultQuery1-30minutes --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --create --topic resultQuery1-1Days --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --create --topic resultQuery1-Global --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --create --topic resultQuery2-30minutes --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --create --topic resultQuery2-1hour --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --create --topic resultQuery2-1day --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --create --topic resultQuery3-30minutes --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --create --topic resultQuery3-1hour --bootstrap-server localhost:9092
docker exec -it broker /bin/kafka-topics --create --topic resultQuery3-1day --bootstrap-server localhost:9092