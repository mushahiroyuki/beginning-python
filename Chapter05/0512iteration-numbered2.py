# ファイル名 Chapter05/0512iteration-numbered2.py
strings = ["あいうえお", 'xxxyyy', "αxxβyyγ"]
print(strings)
for index, string in enumerate(strings):
    if 'xxx' in string:
        strings[index] = '[検閲削除]'
print(strings)
