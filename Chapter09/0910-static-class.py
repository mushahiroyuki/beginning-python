#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter09/0910-static-class.py
class MyClass:
    def smeth():
        print('これはスタティックメソッドです')
    smeth = staticmethod(smeth)
    def cmeth(cls):
        print(f'これは{cls}のクラスメソッドです')
    cmeth = classmethod(cmeth)
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#実行
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
