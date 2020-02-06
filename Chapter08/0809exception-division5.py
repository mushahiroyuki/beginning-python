#ファイル名 Chapter08/0809exception-division5.py
try:
    x = int(input('最初の数を入れてください: '))
    y = int(input('2番目の数を入れてください: '))
    print(x / y)
except (ZeroDivisionError, ValueError) as e:
    print(e)

