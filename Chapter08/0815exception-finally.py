#ファイル名 Chapter08/0815exception-finally.py
x = None
try:
    x = 1 / 0
except Exception as e:
    print('不正な入力です:', e)
    print('処理を継続します。')
finally:
    print('後始末中...')
    del x

print("さらに処理を継続します")
