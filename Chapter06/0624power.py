#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter06/0624power.py
def power(a, n):
    result = 1
    for i in range(n):
        result *= a
    return result
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#実行
for i in range(2,11):
    for j in range(2,11):
        print('{}の{}乗= {}'.format(i, j, power(i,j)))
