#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
# ファイル名 Chapter10/1013-deques.py
from collections import deque
q = deque(range(5))
q.append(5)
q.appendleft(6)
print(q) #← deque([6, 0, 1, 2, 3, 4, 5])
print(q.pop()) #← 5
print(q.popleft()) #← 6
q.rotate(3)
print(q) #← deque([2, 3, 4, 0, 1])
q.rotate(-1)
print(q) #← deque([3, 4, 0, 1, 2])
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
