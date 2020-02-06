# ファイル名 Chapter05/0509name4.py
name = ''
while not name.strip():
    name = input('名前を入力してください：')
print('こんにちは、{}さん!'.format(name))


