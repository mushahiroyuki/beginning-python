# ファイル名 Chapter05/0514while-true.py
while True:
    word = input('単語を入力してください: ')
    if not word: break
    print(f'単語は「{word}」でした。') # 入力された単語に対する処理
