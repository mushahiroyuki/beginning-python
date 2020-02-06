#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter15/1502powers-of-two.py
def powers(n=10):
    return ', '.join(str(2**i) for i in range(n))
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

print(powers(10))


