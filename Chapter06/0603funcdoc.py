#ファイル名 Chapter06/0603funcdoc.py
def square(x):
    '数xの自乗を計算する。'
    return x * x

print(square.__doc__)
print(square(9))
help(square)

 
