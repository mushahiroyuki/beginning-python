# ファイル名 Chapter11/1109-writelines.py
f = open('somefile2.txt')
lines = f.readlines()
f.close()
lines[1] = "isn't a\n"
f = open('somefile3.txt', 'w')
f.writelines(lines)
f.close()
