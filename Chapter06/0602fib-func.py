#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter06/0602fib-func.py
def fibs(num):
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#実行
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
print(fibs(10))
print(fibs(15))
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
