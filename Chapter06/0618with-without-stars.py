#ファイル名 Chapter06/0618with-without-stars.py
def with_stars(**kwds):
    print(f"{kwds['name']}は{kwds['age']}歳です。")
def without_stars(kwds):
    print(f"{kwds['name']}は{kwds['age']}歳です。")

args = {'name': '太郎', 'age': 42}

with_stars(**args) #←太郎は42歳です。
without_stars(args) #←太郎は42歳です。
