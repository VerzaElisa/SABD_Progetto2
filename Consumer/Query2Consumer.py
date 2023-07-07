from confluent_kafka import Consumer
import time as Time
HEADER="TS,ID,Delta1\n"
################
c=Consumer({'bootstrap.servers':'localhost:9092','group.id':'python-consumerQuery2','auto.offset.reset':'latest'})
print('Kafka Consumer has been initiated...')

print('Available topics to consume: ', c.list_topics().topics)
c.subscribe(["resultQuery2-30minutes","resultQuery2-1hour", "resultQuery2-1day"])
################
def main():
    file1=open("../Result/Query2/ResultQuery2-30minutes.csv","w")
    file2=open("../Result/Query2/ResultQuery2-1hour.csv","w")
    file3=open("../Result/Query2/ResultQuery2-1day.csv","w")
    file1.write(HEADER)
    file2.write(HEADER)
    file3.write(HEADER)
    start=Time.time()
    while Time.time()-start<3*60:   #3minuti
        msg=c.poll(1.0) #timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data=msg.value().decode('utf-8')
        start=Time.time()
        print(data)
        if msg.topic()=="resultQuery2-30minutes":
            file1.write(data+"\n")
            file1.flush()
            continue
        if msg.topic()=="resultQuery2-1hour":
            file2.write(data+"\n")
            file2.flush()
            continue
        if msg.topic()== "resultQuery2-1day":
            file3.write(data+"\n")
            file3.flush()
            continue
    c.close()
    file1.close()
    file2.close()
    file3.close()
if __name__ == '__main__':
    main()