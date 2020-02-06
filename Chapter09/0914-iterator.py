#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter09/0914-iterator.py
class TestIterator:
    value = 0
    def __next__(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value
    def __iter__(self):
        return self
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
#実行
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
ti = TestIterator()
print(list(ti)) #← [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
