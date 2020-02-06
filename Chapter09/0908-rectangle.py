#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter09/0908-rectangle.py
class Rectangle:  # 四角形
    def __init__(self):
        self.width = 0  # 幅
        self.height = 0  # 高さ
    def set_size(self, size):
        self.width, self.height = size
    def get_size(self):
        return self.width, self.height
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#実行
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
r = Rectangle()
r.width = 10
r.height = 5
print(r.get_size()) #← (10, 5)
r.set_size((150, 100))
print(r.width) #← 150
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
