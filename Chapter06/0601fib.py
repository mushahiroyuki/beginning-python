#ファイル名 Chapter06/0601fib.py
fibs = [0, 1]
num = int(input('フィボナッチ数をいくつ計算しますか？ '))  # 整数を入力してもらう
for i in range(num-2):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)
