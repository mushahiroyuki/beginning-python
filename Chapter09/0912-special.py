#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter09/0912-special.py
class Rectangle:
    def __init__ (self):
        self.width = 0
        self.height = 0
    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value
        else:
            self. __dict__[name] = value
    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError()
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
#実行
