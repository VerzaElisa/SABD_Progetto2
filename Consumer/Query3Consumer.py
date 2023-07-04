from confluent_kafka import Consumer
################
c=Consumer({'bootstrap.servers':'localhost:9092','group.id':'python-consumer2'})
print('Kafka Consumer has been initiated...')

print('Available topics to consume: ', c.list_topics().topics)
c.subscribe(['resultQuery3-30minutes','resultQuery3-1hour','resultQuery3-1Days'])
################
def main():
    file1=open("../Result/Query3/ResultQuery3-30minutes.csv","w")
    file2=open("../Result/Query3/ResultQuery3-1days.csv","w")
    file3=open("../Result/Query3/ResultQuery3-1hour.csv","w")
    while True:
        msg=c.poll(1.0) #timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data=msg.value().decode('utf-8')
        print(len(data))
        if msg.topic()=="resultQuery3-30minutes":
            file1.write(data+"\n")
            continue
        if msg.topic()=="resultQuery3-1hour":
            file2.write(data+"\n")
            continue
        if msg.topic()=="resultQuery3-1Day":
            file3.write(data+"\n")  
            continue
    c.close()
    file1.close()
    file2.close()
    file3.close()
if __name__ == '__main__':
    main()