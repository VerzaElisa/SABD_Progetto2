import datetime
import time
from typing import Iterable
from operator import itemgetter
from pyflink.datastream.window import TimeWindow
from pyflink.common.watermark_strategy import TimestampAssigner
from pyflink.datastream.functions import ReduceFunction ,ProcessWindowFunction, ProcessAllWindowFunction
#libreria per il quantile dinamico
from psquare.psquare import PSquare

format = "%d-%m-%Y|%H:%M:%S.%f"

def toString(f):
    s=""
    for i in range(len(f)-1):
        s=s+str(f[i])+","
    s=s+str(f[len(f)-1])
    return s
def csvToList(f):
    x=f.split(sep=",")
    return x
class ReduceFunctionQuery1(ReduceFunction):
    def reduce(self,a,b):
        return [b[0],(a[1][0]+b[1][0],a[1][1]+b[1][1])]
        
class CountWindowProcessFunctionPerc(ProcessWindowFunction):    
    def process(self, key: str, context: ProcessWindowFunction.Context[TimeWindow], elements: Iterable[tuple]):
        x=sorted(elements, key=itemgetter(5))
#               |id     | variazione                   | timestamp             | PSquare-25 | PSquare-50 | PSquare-75 | counter | 25-esimo | 50-esimo | 75-esimo  |
        return [[x[0][0],float(x[-1][2])-float(x[0][2]), context.window().start, PSquare(25), PSquare(50), PSquare(75), 0       , ''       , ''       , ''        ]]

class CountWindowProcessFunction(ProcessWindowFunction):    
    def process(self, key: str, context: ProcessWindowFunction.Context[TimeWindow], elements: Iterable[tuple]):
        x=sorted(elements, key=itemgetter(5))
        return [[x[0][0],float(x[-1][2])-float(x[0][2]),context.window().start]]

class Chart(ProcessAllWindowFunction):
    def process(self, ctx, elements):
        x=sorted(elements, key=itemgetter(1))
        res = x[:5]+x[-5:]
        return sorted(res, key=itemgetter(1), reverse=True)

class  OurTimestampAssigner(TimestampAssigner):
    def extract_timestamp(self, value, record_timestamp):
        element = datetime.datetime.strptime(value[4]+"|"+value[3],"%d-%m-%Y|%H:%M:%S.%f")
        timestamp = datetime.datetime.timestamp(element)
        return timestamp*1000
class ReduceFunctionMin(ReduceFunction):
    def reduce(self, a, b):
        time1 = datetime.datetime.strptime(a[4]+"|"+a[3], format)
        time1 = datetime.datetime.timestamp(time1)
        time2 = datetime.datetime.strptime(b[4]+"|"+b[3], format)
        time2 = datetime.datetime.timestamp(time2)
        if time1<time2:
            return a[0], a[1], a[2], a[3], a[4]
        else:
            return b[0], b[1], b[2], b[3], b[4]   
class ReduceFunctionMax(ReduceFunction):
    def reduce(self, a, b):
        time1 = datetime.datetime.strptime(a[4]+"|"+a[3], format)
        time1 = datetime.datetime.timestamp(time1)
        time2 = datetime.datetime.strptime(b[4]+"|"+b[3], format)
        time2 = datetime.datetime.timestamp(time2)
        if time1>time2:
            return a[0], a[1], a[2], a[3], a[4]
        else:
            return b[0], b[1], b[2], b[3], b[4]
class queryADDTimestamp(ProcessWindowFunction):
    def process(self,key,context,elements):
        elements_out=[]
        for e in elements:
            elements_out.append([context.window().start]+list(e))
        return elements_out
class MyMapperMeter(MapFunction):
    def __init__(self):
        self.meter = None
        self.start = time.time()
        self.count = 0
        self.tp = 0.0

    def open(self, runtime_context):
        self.meter = runtime_context\
            .get_metrics_group()\
            .gauge("my_g", lambda :self.tp*1000)
        self.start = time.time()

    def map(self, value: str):
        end = (time.time()-self.start)
        self.count += 1
        self.tp = self.count/end
        return value