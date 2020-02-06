#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter06/0611print-params2.py
def print_params_2(title, *params):
    print(title)
    print(params)

#実行
print_params_2('引数：', 1, 2, 3)
print_params_2('引数はこれだけ：')
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
