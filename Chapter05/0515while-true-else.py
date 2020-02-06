# ファイル名 Chapter05/0515while-true-else.py
from math import sqrt
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("見つかりませんでした。")
