import csv
import time
from confluent_kafka import Producer
from faker import Faker
from datetime import datetime
import logging
import pandas as pd
import numpy as np


fake=Faker()

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='producer.log',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

####################
p=Producer({'bootstrap.servers':'localhost:9092'})
print('Kafka Producer has been initiated...')
#####################
def receipt(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
        print(message)
        
#####################

def main():
    print("Eliminazione header")
    formato = "%d-%m-%Y %H:%M:%S.%f"
    with open("out600_combined+header.csv", "r") as input:
        with open("temp.csv", "w") as output:
            for line in input:
                if not line.strip("\n").startswith('#'):
                    output.write(line)
    print("Lettura chunk csv")
    chunk = pd.read_csv('temp.csv',chunksize=1000000,skiprows=1, header=None, low_memory=False)
    data = pd.concat(chunk)

    print("Ordinamento e creazione data")
    data=data.sort_values(by=[2,3])
    data["NewDate"]=data[2].astype(str)+' '+data[3].astype(str)
    data["NewDate"] = pd.to_datetime(data["NewDate"], format=formato)
    data['Differenza'] = data['NewDate'].diff().dt.total_seconds() * 1000
    line = data.iloc[0].to_string(index=False).replace(' ','').replace('\n',',')
    for i in range(1, len(data.index)):
        p.poll(1)
        p.produce('user-tracker', line.encode('utf-8'),callback=receipt)
        p.flush()
        line = data.iloc[i]
        if(line["Differenza"]!=0.0):
            time.sleep(line["Differenza"]/100)
        line=line.to_string(index=False).replace(' ','').replace('\n',',')
    print(line)

if __name__ == '__main__':
    main()