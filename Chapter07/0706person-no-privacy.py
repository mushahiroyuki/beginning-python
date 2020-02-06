#ファイル名 Chapter07/0706person-no-privacy.py
# __metaclass__ = type #← python 2を使っている場合は行頭の「#」を取る。以下省略
class Person:
    def set_name(self, name):
         self.name = name
    def get_name(self):
         return self.name
    def greet(self): # あいさつをする
         print(f"こんにちは。私は{self.name}です。")

#実行
foo = Person()
bar = Person()
foo.set_name('ルーク・スカイウォーカー') #『スター・ウォーズ』の主要登場人物
bar.set_name('アナキン・スカイウォーカー') # ルークの父

print(foo.name) #← ルーク・スカイウォーカー
foo.name = 'ガンビー'
print(foo.get_name()) #← ガンビー
