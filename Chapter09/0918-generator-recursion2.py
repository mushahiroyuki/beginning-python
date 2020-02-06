#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter09/0918-generator-recursion2.py
def flatten(nested):
    try:
        # 文字列に類するオブジェクトはイテレーションしない
        try: nested + ''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
fl = list(flatten(['foo', ['bar', ['baz']]]))
print(fl) #← ['foo', 'bar', 'baz']
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
