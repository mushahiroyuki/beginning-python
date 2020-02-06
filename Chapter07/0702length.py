#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter07/0702length.py
def length_message(x):
    print(repr(x), "の長さは", len(x), "です")
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

length_message('Fnord')
length_message([1, 2, 3])

