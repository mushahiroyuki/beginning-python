# ファイル名 Chapter02/listing2-2.py
# https://www.xxx.yyy の形式のURLから、xxxの部分を取り出す

url = input('URLを入力してください: ')
domain = url[12:-4]

print("結果: " + domain)
