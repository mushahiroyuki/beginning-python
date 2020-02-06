#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter09/0917-generator-recursion.py
def flatten(nested):
    try:
        for sublist in nested: # ネストの場合
            for element in flatten(sublist): # sublistをflattenした各要素を順に
                yield element # 呼び出し側に返す（yieldする）
    except TypeError: # nestedがリストでない場合
        yield nested
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
fl = list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8]))
print(fl) #← [1, 2, 3, 4, 5, 6, 7, 8]
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list3)  # ←この行は無視してください。本文に引用するためのものです。
#fl = list(flatten([[["33"], 2], 3, 4, [5, [6, 7]], 8]))  #←例外
#@@range_end(list3)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list3)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_end(list3)  # ←この行は無視してください。本文に引用するためのものです。
