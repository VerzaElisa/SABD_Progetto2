from confluent_kafka import Consumer
import time as Time
HEADER="TS,ID,Count,AVG_Last_value\n"
################
c=Consumer({'bootstrap.servers':'localhost:9092','group.id':'python-consumerQuery1','auto.offset.reset':'latest'})
print('Kafka Consumer has been initiated...')

print('Available topics to consume: ', c.list_topics().topics)
c.subscribe(['resultQuery1-1hour','resultQuery1-1Days','resultQuery1-Global'])
################
def main():
    file1=open("../Result/Query1/ResultQuery1-1hour.csv","w")
    file2=open("../Result/Query1/ResultQuery1-1days.csv","w")
    file3=open("../Result/Query1/ResultQuery1-global.csv","w")
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
        print(data)
        start=Time.time()
        if msg.topic()=="resultQuery1-1hour":
            file1.write(data+"\n")
            file1.flush()
            continue
        if msg.topic()=="resultQuery1-1Days":
            file2.write(data+"\n")
            file2.flush()
            continue
        if msg.topic()=="resultQuery1-Global":
            file3.write(data+"\n")  
            file3.flush()
            continue
    c.close()
    file1.close()
    file2.close()
    file3.close()
if __name__ == '__main__':
    main()