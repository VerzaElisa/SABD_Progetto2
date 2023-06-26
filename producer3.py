from confluent_kafka import Producer
import json
import time
import logging
import random
import pandas as pd
import numpy as np
import csv
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
def f(r):
    s=''
    for i in r[:38]:
        s=s+i+','
    return s+r[38]
def main():
    #data=pd.read_csv(filepath_or_buffer="../../../Download/out600_combined+header.csv",skiprows=12,low_memory=False,header=None)
    #print(data)
    with open("dataset.csv") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            p.poll(1)
            p.produce('user',f(row),callback=receipt)
            p.flush
            if float(f[41]) != 0.0:
                time.sleep(f[41]/3600*1000)
        csv_file.close()
if __name__ == '__main__':
    main()