# ファイル名 Chapter04/listing4-1.py
# 単純なデータベース

# 辞書peopleには人名（名字）をキーとして、内線番号と社内連絡用のメールアドレスが記憶されている別の辞書が記憶されている
# 
people = {
    '渋谷': {
        '内線': '2341',
        'メール': 'taro-shibuya'
    },
    '恵比寿': {
        '内線': '9102',
        'メール': 'hanako-ebisu'
    },
    '上野': {
        '内線': '3158',
        'メール': 'jiro-ueno'
    }
}

# ユーザーに表示するメッセージと記憶するデータのキーとの対応を記憶
labels = {
    '内線': '内線番号',
    'メール': 'メールアドレス'
}

name = input('名前を入れてください：')

# 内線番号を調べるのか、メールアドレスを調べるのか尋ねる
request = input('内線電話は t を、メールアドレスは m を入れてください：')

if request == 't': key = '内線'
if request == 'm': key = 'メール'

# 名前が辞書にあれば要求された情報を出力する
if name in people: print(f"{name}さんの{labels[key]}は {people[name][key]} です。")

#@# if name in people: print("{}さんの{}は {} です。".format(name, labels[key], people[name][key]))
