#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter06/0623factorial-recursion.py
def factorial(n):
    if n == 1:
       return 1
    else:
       return n * factorial(n - 1)
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

# 実行
for i in range(1,11):
    print('{}! = {}'.format(i, factorial(i)))
