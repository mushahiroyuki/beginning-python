#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter11/listing11-10.py
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
def process(string):
    print('処理中:', string)

filename = "somefile.txt"

#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
with open(filename) as f:
    for line in f.readlines():
        process(line)
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
