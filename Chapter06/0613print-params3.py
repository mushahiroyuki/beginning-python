#ファイル名 Chapter06/0613print-params3.py
def print_params_3(**params):
    print(params)

#実行
print_params_3(x=1, y=2, z=3) #←{'x': 1, 'y': 2, 'z': 3}
