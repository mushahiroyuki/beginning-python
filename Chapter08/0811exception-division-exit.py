#ファイル名 Chapter08/0811exception-division-exit.py
try:
    x = int(input('最初の数を入れてください: '))
    sys.exit #←終了する
    y = int(input('2番目の数を入れてください: '))
    print(x / y)
except:
    print('何らかの不具合が起こりました')
