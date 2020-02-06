# ファイル名 Chapter11/1108-write.py
f = open('somefile2.txt', 'w')
print(f.write('this\nis no\nhaiku\n'))  #← 17 （17文字書き込んだ）
print(f.write('これは\n俳句では\nありません')) #← 14  （14文字書き込んだ）
f.close()
