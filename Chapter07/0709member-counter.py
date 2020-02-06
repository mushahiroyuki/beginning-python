#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter07/0709member-counter.py
class MemberCounter:
    members = 0
    def init(self):
        MemberCounter.members += 1

#実行
m1 = MemberCounter()
m1.init()
print(MemberCounter.members) #←1
m2 = MemberCounter()
m2.init()
print(MemberCounter.members) #←2
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
print(m1.members) #←2
print(m2.members) #←2
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list3)  # ←この行は無視してください。本文に引用するためのものです。
m1.members = 'Two'
print(m1.members) #←Two
print(m2.members) #←2
#@@range_end(list3)  # ←この行は無視してください。本文に引用するためのものです。
