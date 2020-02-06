#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter09/0903-1inherit.py
class A:
    def hello(self):
        print("こんにちは、Aです。")
class B(A):
    pass
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#実行
a = A()
b = B()
a.hello()
b.hello()
