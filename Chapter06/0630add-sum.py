#ファイル名 Chapter06/0630add-sum.py
numbers = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
from functools import reduce
from operator import add #←モジュールoperatorのaddをインポート
print(reduce(add, numbers)) #←addを第1引数の関数に指定
print(sum(numbers)) #←組み込み関数のsumを使う

