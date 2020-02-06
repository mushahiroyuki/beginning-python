#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter08/0819-attribute-check.py
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
class Something:
    write = True
    read = False

obj = Something()
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
try:
    obj.write
except AttributeError:
    print('このオブジェクトは書き込み可能ではない。')
else:
    print('このオブジェクトは書き込み可能である。')
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
