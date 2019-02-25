import time
from datetime import datetime
seconds = time.time()
print(seconds)

# time.struct_time(tm_year=2019, tm_mon=2, tm_mday=22, tm_hour=16, tm_min=8, tm_sec=8, tm_wday=4, tm_yday=53, tm_isdst=0)
time_tuple = time.localtime(seconds)
print(time_tuple)

time_string1 = time.asctime(time_tuple)
print(time_string1)

time_string2 = time.ctime(time.time())
print(time_string2)

time_format1 = time.strftime('%Y-%m-%d %H:%M:%S', time_tuple)
print(time_format1)

time_format2 = time.strftime('%m/%d/%Y %H:%M:%S', time_tuple)
print(time_format2)

print("***********************datetime*********************")
#************************** datetime *********************************
now1 = datetime.now()
print(now1)
print(now1.year)

now2 = datetime.fromtimestamp(time.time())
print(now2)

