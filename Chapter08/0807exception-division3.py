#ファイル名 Chapter08/0807exception-division3.py
try:
    x = int(input('最初の数を入れてください: '))
    y = int(input('2番目の数を入れてください: '))
    print(x / y)
except ZeroDivisionError:
    print("2番目の数は0であってはなりません!")
except ValueError:
   print("数値を指定してください！")
