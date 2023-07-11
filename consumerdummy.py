from confluent_kafka import Consumer
import time as Time

################
c=Consumer({'bootstrap.servers':'localhost:9092','group.id':'dummy','auto.offset.reset':'latest'})
c.subscribe(['user2'])
################
HEADER="TS,ID,value,Count\n"
def main():
    while True:   #3minuti
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