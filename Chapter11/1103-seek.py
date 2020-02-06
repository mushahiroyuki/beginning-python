#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
# ファイル名 Chapter11/1103-seek.py
f = open('somefile.txt', 'w')
print(f.write('01234567890123456789')) #← 20
print(f.seek(5)) #← 5
print(f.write('Hello, World!')) #← 13
f.close()
f = open('somefile.txt')
print(f.read()) #← 01234Hello, World!89
f.close()
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
f = open('somefile.txt')
print(f.read(3)) #← 012
print(f.read(2)) #← 34
print(f.tell()) #← 5
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
