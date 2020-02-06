# ファイル名 Chapter10/1016-random-dice.py
from random import randrange
num   = int(input('サイコロはいくつですか？ '))
sides = int(input('各サイコロには面がいくつありますか？ '))
sum = 0
for i in range(num):
    j = randrange(sides) + 1
    print(f'{i+1}個目: {j}')
    sum += j
print(f'---------\n合計: {sum}')
