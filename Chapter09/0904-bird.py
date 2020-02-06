#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter09/0904-bird.py
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('いただきます！')
            self.hungry = False
        else:
            print('お腹いっぱい！')
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
class SongBird(Bird):
    def __init__(self):
        self.sound = 'ホー、ホケキョ！'
    def sing(self):
        print(self.sound)
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。

#実行
#@@range_begin(list3)  # ←この行は無視してください。本文に引用するためのものです。
b = Bird()
b.eat() #← いただきます！
b.eat() #← お腹いっぱい！
#@@range_end(list3)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list4)  # ←この行は無視してください。本文に引用するためのものです。
sb = SongBird()
sb.sing() #← ホー、ホケキョ！
#@@range_end(list4)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list5)  # ←この行は無視してください。本文に引用するためのものです。
sb.eat()
#@@range_end(list5)  # ←この行は無視してください。本文に引用するためのものです。


