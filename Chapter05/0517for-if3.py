# ファイル名 Chapter05/0517for-if3.py
#squares = {i: "{}の2乗は{}".format(i, i**2) for i in range(10)} #←こちらでも可
squares = {i: f"{i}の2乗は{i**2}" for i in range(10)}
print(squares[8])
#for i in range(10):
#    print(squares[i])

