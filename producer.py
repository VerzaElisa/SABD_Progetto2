from confluent_kafka import Producer
from faker import Faker
import json
import time
import logging
import random
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
    data=pd.read_csv(filepath_or_buffer="../../out500_combined+header.csv",skiprows=[0,1,2,3,4,5,6,7,8,9,10,11,12],low_memory=False,header=None)
    print(data)
    data2=data.sort_values(by=['Date','Time'])
    data2["Date"]=data2["Date"].astype(str)
    data2["Time"]=data2["Time"].astype(str)
    data2["NewDate"]=data2["Date"]+data2["Time"]
    print(data2) 
    for i in range(len(data2.index)):
        x=data2.loc[i]
        print(x)
        p.poll(1)
        p.produce('user-tracker',x.to_csv(header=False),callback=receipt)
        p.flush
        print(str(x['Date']))
        time.sleep(10)
    
    #    data={
    #       'user_id': fake.random_int(min=20000, max=100000),
    #       'user_name':fake.name(),
    #       'user_address':fake.street_address() + ' | ' + fake.city() + ' | ' + fake.country_code(),
    #       'platform': random.choice(['Mobile', 'Laptop', 'Tablet']),
    #       'signup_at': str(fake.date_time_this_month())    
    #       }
    #    m=json.dumps(data)
    #    p.poll(1)
    #    p.produce('user-tracker', m.encode('utf-8'),callback=receipt)
    #    p.flush()
    #    time.sleep(3)
        
if __name__ == '__main__':
    main()