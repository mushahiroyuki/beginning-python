#ファイル名 Chapter07/0711inheritance.py
class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter): #←SPAMFilterはFilterのサブクラス
    def init(self): #←スーパクラスのinitをオーバライド
        self.blocked = ['SPAM']

class SpecialSPAMFilter(SPAMFilter):
    def init(self): #←スーパクラスのinitをオーバライド
        self.blocked = ['SPECIALSPAM']
        
#実行
print(SpecialSPAMFilter.__bases__) #←(<class '__main__.SPAMFilter'>,)
print(SPAMFilter.__bases__) #←(<class '__main__.Filter'>,)
print(Filter.__bases__) #←(<class 'object'>,)
