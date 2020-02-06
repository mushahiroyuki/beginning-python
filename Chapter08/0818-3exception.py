#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter08/0818-3exception.py
def describe_person(person):
    print(f"{person['氏名']}に関する記述：")
    print(f"年齢: {person['年齢']}")
    try:
        print(f"職業: {person['職業']}")
    except KeyError: pass
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#実行
yamada = {"氏名": "山田太郎", "年齢": 42, "職業": "プログラマー"}
describe_person(yamada)
kato = {"氏名": "加藤次郎", "年齢": 30}
describe_person(kato)
