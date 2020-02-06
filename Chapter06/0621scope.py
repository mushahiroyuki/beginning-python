#ファイル名 Chapter06/0621scope.py
x = 1
scope = vars()
print(scope['x'])

scope['x'] += 1
print(x)
