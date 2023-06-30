from confluent_kafka import Consumer
################
c=Consumer({'bootstrap.servers':'localhost:9092','group.id':'python-consumer','auto.offset.reset':'earliest'})
print('Kafka Consumer has been initiated...')

print('Available topics to consume: ', c.list_topics().topics)
c.subscribe(['resultQuery1-30minutes','resultQuery1-1Days'])
################
def main():
    c1=0
    c2=0
    c3=0
    file1=open("./Result/Query1/ResultQuery1-30minutes.csv","w")
    file2=open("./Result/Query1/ResultQuery1-1days.csv","w")
    file3=open("./Result/Query1/ResultQuery1-global.csv","w")
    while True:
        msg=c.poll(1.0) #timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data=msg.value().decode('utf-8')
        if msg.topic()=="resultQuery1-30minutes":
            file1.write(data+"\n")
            c1=c1+1
            print("30-minutes: ",c1)
            file1.flush()
            continue
        if msg.topic()=="resultQuery1-1Days":
            file2.write(data+"\n")
            c2=c2+1
            print("1-days: ",c2)
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