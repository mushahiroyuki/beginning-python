#ファイル名 Chapter08/0814exception-except-exception.py
while True:
    try:
        x = int(input('最初の数を入れてください: '))
        y = int(input('2番目の数を入れてください: '))
        value = x / y
        print(f'{x}/{y}は{value}です。')
    except Exception as e:
        print('不正な入力です:', e)
        print('もう一度入力してください。')
    else:
        break
