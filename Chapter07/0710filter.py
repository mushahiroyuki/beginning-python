#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter07/0710filter.py
class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter): #←SPAMFilterはFilterのサブクラス
    def init(self): #←スーパクラスのinitをオーバライド
        self.blocked = ['SPAM']
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#実行
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
f = Filter()
f.init()
print(f.filter([1, 2, 3])) #← [1, 2, 3]
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list3)  # ←この行は無視してください。本文に引用するためのものです。
s = SPAMFilter()
s.init()
print(s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM']))
#↑ ['eggs', 'bacon']
#@@range_end(list3)  # ←この行は無視してください。本文に引用するためのものです。

