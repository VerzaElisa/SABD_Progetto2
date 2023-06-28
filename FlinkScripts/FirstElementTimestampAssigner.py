import datetime

from pyflink.common.watermark_strategy import TimestampAssigner


class FirstElementTimestampAssigner(TimestampAssigner):
    def extract_timestamp(self, value, record_timestamp):
        element = datetime.datetime.strptime(value[4]+"|"+value[3],"%d-%m-%Y|%H:%M:%S.%f")
        timestamp = datetime.datetime.timestamp(element)
        return timestamp*1000