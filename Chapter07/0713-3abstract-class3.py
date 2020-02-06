#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter07/0713-3abstract-class3.py
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
from abc import ABC, abstractmethod
class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass

#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
class FrequentTalker(Talker): #頻繁に話す人
    def talk(self):
        print("こんにちは!")

#実行
ft = FrequentTalker()
print(isinstance(ft, Talker)) #←True
ft.talk() #←こんにちは
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list3)  # ←この行は無視してください。本文に引用するためのものです。
print(isinstance(ft, FrequentTalker)) #←True
#@@range_end(list3)  # ←この行は無視してください。本文に引用するためのものです。
