#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter08/0818-1if.py
def describe_person(person): #← 人を描写する
    print(f"{person['氏名']}に関する記述：")
    print(f"年齢: {person['年齢']}")
    if '職業' in person:
        print(f"職業: {person['職業']}")
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#実行
yamada = {"氏名": "山田太郎", "年齢": 42}
describe_person(yamada)
