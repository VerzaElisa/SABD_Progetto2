from confluent_kafka import Consumer
import time as Time
################
c=Consumer({'bootstrap.servers':'localhost:9092','group.id':'python-consumerQuery3','auto.offset.reset':'latest'})
print('Kafka Consumer has been initiated...')

print('Available topics to consume: ', c.list_topics().topics)
c.subscribe(['resultQuery3-30minutes','resultQuery3-1hour','resultQuery3-1day'])
################
HEADER="TS,Mercato,25percentile,50percentile,75percentile\n"
def main():
    file1=open("../Result/Query3/ResultQuery3-30minutes.csv","w")
    file2=open("../Result/Query3/ResultQuery3-1hour.csv","w")
    file3=open("../Result/Query3/ResultQuery3-1days.csv","w")
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
        if msg.topic()=="resultQuery3-30minutes":
            file1.write(data+"\n")
            file1.flush()
            continue
        if msg.topic()=="resultQuery3-1hour":
            file2.write(data+"\n")
            file2.flush()
            continue
        if msg.topic()=="resultQuery3-1day":
            print(data)
            file3.write(data+"\n")
            file3.flush()
            continue
    c.close()
    file1.close()
    file2.close()
    file3.close()
if __name__ == '__main__':
    main()