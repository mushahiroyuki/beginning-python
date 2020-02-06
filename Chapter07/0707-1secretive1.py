#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter07/0707-1secretive1.py
class Secretive: #秘密にされた（もの）

    def __inaccessible(self): #アクセスできない
        print("あなたは私が見えない。")
    def accessible(self): #アクセス可能
        print("秘密のメッセージ：", end="") #←end=は第5章参照
        self.__inaccessible()
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#実行
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
s = Secretive()
s.accessible()
s.__inaccessible()
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。

print(Secretive._Secretive__inaccessible)
s._Secretive__inaccessible()

