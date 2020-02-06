# ファイル名 Chapter10/1017-random-fortune.py
import fileinput, random
fortunes = list(fileinput.input())
print(random.choice(fortunes))
