#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
# ファイル名 Chapter10/1012-heap2.py
from heapq import *
heap = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
heapify(heap)
print(heap)  #← [0, 1, 5, 3, 2, 7, 9, 8, 4, 6]
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
print(heapreplace(heap, 0.5)) #← 0
print(heap) #← [0.5, 1, 5, 3, 2, 7, 9, 8, 4, 6]
print(heapreplace(heap, 10)) #← 0.5
print(heap) #← [1, 2, 5, 3, 6, 7, 9, 8, 4, 10]
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
