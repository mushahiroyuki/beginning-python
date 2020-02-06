#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter06/0622factorial.py
def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

# 実行
for i in range(1,11):
    print('{}! = {}'.format(i, factorial(i)))
