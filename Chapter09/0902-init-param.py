#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter09/0902-init-param.py
class FooBar:
    def __init__(self, value=42):
       self.somevar = value
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#実行
f = FooBar('これはコンストラクタの引数です')
print(f.somevar)
g = FooBar()
print(g.somevar)

