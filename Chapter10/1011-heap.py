#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
# ファイル名 Chapter10/1011-heap.py
from heapq import *
from random import shuffle
data = list(range(10))
shuffle(data)
heap = []
for n in data:
    heappush(heap, n)

print(heap) #← [0, 1, 2, 6, 5, 4, 3, 9, 7, 8]   ←例（毎回異なる）
heappush(heap, 0.5)
print(heap) #← [0, 0.5, 2, 6, 1, 4, 3, 9, 7, 8, 5]
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
print(heappop(heap)) #← 0
print(heappop(heap)) #← 0.5
print(heappop(heap)) #← 1
print(heap) #← [2, 5, 3, 6, 8, 4, 7, 9]
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
