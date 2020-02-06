#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter07/0713-2abstract-class2.py
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
from abc import ABC, abstractmethod
class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass

#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
class FrequentTalker(Talker): #頻繁に話す人
    pass
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。

#実行
FrequentTalker()
