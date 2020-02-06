#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter06/0625power-recursion.py
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#実行
for i in range(2,11):
    for j in range(2,11):
        print('{}の{}乗= {}'.format(i, j, power(i,j)))
