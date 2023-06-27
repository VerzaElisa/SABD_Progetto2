from confluent_kafka import Consumer
################
c=Consumer({'bootstrap.servers':'localhost:9092','group.id':'python-consumer','auto.offset.reset':'earliest'})
print('Kafka Consumer has been initiated...')

print('Available topics to consume: ', c.list_topics().topics)
c.subscribe(['resultQuery1-30minutes','resultQuery1-1Days'])
################
def main():
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
            continue
        if msg.topic()=="resultQuery1-1days":
            file2.write(data+"\n")
            continue
        if msg.topic()=="resultQuery1-1days":
            file3.write(data+"\n")
            continue
    c.close()
if __name__ == '__main__':
    main()