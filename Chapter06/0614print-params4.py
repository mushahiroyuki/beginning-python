#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter06/0614print-params4.py
def print_params_4(x, y, z=3, *pospar, **keypar):
    print(x, y, z)
    print(pospar)
    print(keypar)

#実行
print_params_4(1, 2, 3, 5, 6, 7, foo=1, bar=2)
print("----")
print_params_4(1, 2)
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
