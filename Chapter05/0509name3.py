# ファイル名 Chapter05/0509name3.py
name = ''
while not name or name.isspace():
    name = input('名前を入力してください：')
print('こんにちは、{}さん!'.format(name))


