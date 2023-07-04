import csv
import os
import time
from confluent_kafka import Producer
from datetime import datetime
import logging
import pandas as pd
import numpy as np


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
    #else:
    #    message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
    #    logger.info(message)
    #    print(message)
        
#####################
def lint_to_string(r):
    s=''
    for i in r[:38]:
        s=s+i+','
    return s+r[38]

def create_file():
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
    data['Differenza'] = data['Differenza'].shift(-1)
    
    print('Salvataggio su file')
    output_path = 'dataset.csv'
    data.to_csv(output_path, header=False,chunksize = 10000, mode='a', index=False)

def invio():
    print('Inizio invio')
    with open("dataset.csv") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)
            p.produce('user',lint_to_string(row),callback=receipt)
            if row[41]!="" and float(row[41]) != 0.0:
                p.flush()
                time.sleep(float(row[41])/(3600*1000/4)) #1 ora = 4sec circ
        rowFinal=['RigaFinale.END', 'E', '16-11-2021', '09:00:00.000', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '0.0', '0.0', '09:00:00.000', '0.0', '', '16-11-2021', '', '', '', '', '', '', '09:00:00.000', '', '', '', '', '', '', '2021-11-16 09:00:00.000', '0.0']
        p.produce('user',lint_to_string(rowFinal),callback=receipt)
        p.flush()
        csv_file.close()

def main():
    check = os.path.isfile("./dataset.csv")
    if check:
        invio()
    else:
        create_file()
        invio()

if __name__ == '__main__':
    main()