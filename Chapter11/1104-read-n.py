# ファイル名 Chapter11/1104-read-n.py
f = open('somefile.txt')
print(f.read(7)) #← "Welcome"
print(f.read(4)) #← " to "
f.close()
