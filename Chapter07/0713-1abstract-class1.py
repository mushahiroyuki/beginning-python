#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter07/0713-1abstract-class1.py
from abc import ABC, abstractmethod
class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
#実行
Talker()
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
