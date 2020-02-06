#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter07/0703person.py
# __metaclass__ = type #← python 2を使っている場合は行頭の「#」を取る
class Person:
    def set_name(self, name):
         self.name = name
    def get_name(self):
         return self.name
    def greet(self): # あいさつをする
         print(f"こんにちは。私は{self.name}です。")
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#実行
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
foo = Person()
bar = Person()
foo.set_name('ルーク・スカイウォーカー') #『スター・ウォーズ』の主要登場人物
bar.set_name('アナキン・スカイウォーカー') # ルークの父
foo.greet() #←こんにちは。私はルーク・スカイウォーカーです。
bar.greet() #←こんにちは。私はアナキン・スカイウォーカーです。
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list3)  # ←この行は無視してください。本文に引用するためのものです。
print(foo.name) #←ルーク・スカイウォーカー
bar.name = 'ヨーダ'
bar.greet() #←こんにちは。私はヨーダです。
#@@range_end(list3)  # ←この行は無視してください。本文に引用するためのものです。
