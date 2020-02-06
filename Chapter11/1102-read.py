# ファイル名 Chapter11/1102-read.py
f = open('somefile.txt', 'r')
print(f.read(4))  #← Hell
print(f.read())  #← o, World!こんにちは、皆さん！
