#ファイル名 Chapter07/0711inheritance.py
class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter): #←SPAMFilterはFilterのサブクラス
    def init(self): #←スーパクラスのinitをオーバライド
        self.blocked = ['SPAM']

#実行
#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
print(issubclass(SPAMFilter, Filter)) #←True
print(issubclass(Filter, SPAMFilter)) #←False
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
print(SPAMFilter.__bases__) #←(<class '__main__.Filter'>,)
print(Filter.__bases__) #←(<class 'object'>,)
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list3)  # ←この行は無視してください。本文に引用するためのものです。
s = SPAMFilter()
print(isinstance(s, SPAMFilter)) #←True
print(isinstance(s, Filter)) #←True
print(isinstance(s, str)) #←False
#@@range_end(list3)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list4)  # ←この行は無視してください。本文に引用するためのものです。
print(s.__class__) #←<class '__main__.SPAMFilter'>
#@@range_end(list4)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list4)  # ←この行は無視してください。本文に引用するためのものです。
print(type(s)) #←<class '__main__.SPAMFilter'>
f = Filter()
print(type(f)) #←<class '__main__.Filter'>
#@@range_end(list4)  # ←この行は無視してください。本文に引用するためのものです。
