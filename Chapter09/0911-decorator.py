#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter09/0911-decorator.py
class MyClass:
    @staticmethod
    def smeth():
        print('これはスタティックメソッドです')
    @classmethod
    def cmeth(cls):
        print(f'これは{cls}のクラスメソッドです')
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#実行
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
MyClass.smeth() #← これはスタティックメソッドです
MyClass.cmeth() #← これは<class '__main__.MyClass'>のクラスメソッドです
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
