#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
# ファイル名 Chapter10/1015-random.py
from random import *
from time import *
date1 = (2020, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = mktime(date1)
date2 = (2021, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(date2)
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
random_time = uniform(time1, time2)
print(asctime(localtime(random_time))) #← Wed Jan  8 04:32:13 2020   ←例
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
