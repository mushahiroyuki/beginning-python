# ファイル名 Chapter11/1101-write.py
f = open('somefile.txt', 'w')
print(f.write('Hello, '))  #← 7
print(f.write('World!')) #← 6
print(f.write('こんにちは、')) #← 6
print(f.write('皆さん！')) #← 4
f.close()
