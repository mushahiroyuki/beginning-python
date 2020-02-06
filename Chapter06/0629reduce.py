#ファイル名 Chapter06/0629reduce.py
numbers = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
from functools import reduce
print(reduce(lambda x, y: x + y, numbers))

