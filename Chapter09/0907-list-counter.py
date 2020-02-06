#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter09/0907-list-counter.py
class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0
    def __getitem__(self, index):
        self.counter += 1
#@#         return super(CounterList, self).__getitem__(index)
        return super().__getitem__(index)
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#実行
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
cl = CounterList(range(10))
print(cl) #← [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cl.reverse()
print(cl) #← [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
del cl[3:6]
print(cl) #← [9, 8, 7, 3, 2, 1, 0]
print(cl.counter) #← 0
print(cl[4] + cl[2]) #← 9  （← 2+7）
print(cl.counter) #← 2  （←2回アクセスされた）
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
