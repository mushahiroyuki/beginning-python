#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter09/0913-fib.py
class Fibs:
    def __init__(self): #← 初期化
        self.a = 0
        self.b = 1
    def __next__(self): 
        self.a, self.b = self.b, self.a + self.b #← 前の2項を足したものを self.bに準備
        return self.a  #← self.a を返す
    def __iter__(self):
        return self
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
#実行
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f) #← 1597
        break
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。

for f in Fibs():
    if f > 1000:
        print(f) #← 1597
        break
