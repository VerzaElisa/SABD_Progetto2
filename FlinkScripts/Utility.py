import datetime
from typing import Iterable
from operator import itemgetter
from pyflink.datastream.window import TimeWindow
from pyflink.common.watermark_strategy import TimestampAssigner
from pyflink.datastream.functions import ReduceFunction ,ProcessWindowFunction
format = "%d-%m-%Y|%H:%M:%S.%f"

class CountWindowProcessFunction(ProcessWindowFunction):
    def process(self, key: str, context: ProcessWindowFunction.Context[TimeWindow], elements: Iterable[tuple]):
        x=sorted(elements, key=itemgetter(2))
        return [[x[0][0],float(x[-1][2])-float(x[0][2]),context.window().start, context.window().end]]
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
