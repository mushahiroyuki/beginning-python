#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter11/listing11-14.py
#実行例:  python3 listing11-14.py < somefile.txt

import sys
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
def process(string):
    print('処理中:', string)
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。

for line in sys.stdin:
    process(line)
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
    
