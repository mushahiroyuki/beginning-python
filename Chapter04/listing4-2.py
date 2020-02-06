# ファイル名 Chapter04/listing4-2.py
# 単純なデータベース。get()を使うバージョン
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

# getを使ってデフォルト値を出力する
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, '未登録')

print("{}さんの{}は {} です。".format(name, label, result))
