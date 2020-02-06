#ファイル名 Chapter08/0810exception-division6.py
try:
    x = int(input('最初の数を入れてください: '))
    y = int(input('2番目の数を入れてください: '))
    print(x / y)
except:
    print('何らかの不具合が起こりました')
