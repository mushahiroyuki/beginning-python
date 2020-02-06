#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter09/0903-2inherit2.py
class A:
    def hello(self):
        print("こんにちは、Aです。")
class B(A):
    def hello(self):
        print("こんにちは、Bです。")
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#実行
a = A()
b = B()
a.hello()
b.hello()
