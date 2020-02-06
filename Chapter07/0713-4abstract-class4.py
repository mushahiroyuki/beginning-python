#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter07/0713-4abstract-class4.py
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
from abc import ABC, abstractmethod
class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass

class FrequentTalker(Talker): #頻繁に話す人
    def talk(self):
        print("こんにちは!")

#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
class NightTalker:
    def talk(self):
        print("こんばんは")
        
#実行
nt = NightTalker()
nt.talk() #←こんばんは
print(isinstance(nt, FrequentTalker)) #←False
print(isinstance(nt, Talker)) #←False
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。

print("--------------1")
#@@range_begin(list3)  # ←この行は無視してください。本文に引用するためのものです。
print(Talker.register(NightTalker)) #←<class '__main__.NightTalker'>
print(isinstance(nt, Talker)) #←True
print(issubclass(NightTalker, Talker)) #←True
#@@range_end(list3)  # ←この行は無視してください。本文に引用するためのものです。

print("--------------2")
#@@range_begin(list4)  # ←この行は無視してください。本文に引用するためのものです。
class Speaker:
      pass

print(Talker.register(Speaker)) #←<class '__main__.Speaker'>
print(issubclass(Speaker, Talker)) #←True
s = Speaker() #←Speakerのインスタンスを生成
print(isinstance(s, Talker)) #←True
s.talk() #下のエラー発生。メソッドtalkは呼び出せない
# 
# Traceback (most recent call last):
#   File "0713-4abstract-class4.py", line 39, in <module>
#     s.talk()
# AttributeError: 'Speaker' object has no attribute 'talk'
# ↑属性エラー: 'Speaker'オブジェクトは'talk'という属性をもっていない
#@@range_end(list4)  # ←この行は無視してください。本文に引用するためのものです。
