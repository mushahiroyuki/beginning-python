# ファイル名 Chapter10/1010-set2.py
from functools import reduce
my_sets = []
for i in range(10):
    my_sets.append(set(range(i, i+5)))

print(reduce(set.union, my_sets)) #← {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

