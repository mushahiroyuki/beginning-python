#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter09/0905-bird2.py
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('いただきます！')
            self.hungry = False
        else:
            print('お腹いっぱい！')

class SongBird(Bird):
    def __init__(self):
        super().__init__() #← この行を追加！
        self.sound = 'ホー、ホケキョ！'
    def sing(self):
        print(self.sound)
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#実行

#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
sb = SongBird()
sb.sing() #← ホー、ホケキョ！
sb.eat() #← いただきます！
sb.eat() #← お腹いっぱい！
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。


