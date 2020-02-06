# ファイル名 Chapter02/listing2-4.py
# ユーザー名と暗証番号の照合

database = [
    ['太郎', '1234'],
    ['花子', '4242'],
    ['スミス', '7524'],
    ['メアリー', '9843']
]

username = input('ユーザー名：')
number = input('暗証番号：')

if [username, number] in database: print('アクセスが許可されました。')
