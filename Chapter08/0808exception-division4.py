#ファイル名 Chapter08/0808exception-division4.py
try:
    x = int(input('最初の数を入れてください: '))
    y = int(input('2番目の数を入れてください: '))
    print(x / y)
except (ZeroDivisionError, ValueError, NameError): #←タプルで指定
    print("割り算のできる数値が指定されていません！")
