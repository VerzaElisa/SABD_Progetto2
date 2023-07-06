from confluent_kafka import Consumer
import time as Time

################
c=Consumer({'bootstrap.servers':'localhost:9092','group.id':'python-consumerQuery1','auto.offset.reset':'latest'})
print('Kafka Consumer has been initiated...')

print('Available topics to consume: ', c.list_topics().topics)
c.subscribe(['spark'])
################
def main():
    start=Time.time()
    while Time.time()-start<5*60*1000:   #5minuti
        msg=c.poll(1.0) #timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data=msg.value().decode('utf-8')
        print(data)
        start=Time.time()
    c.close()
if __name__ == '__main__':
    main()