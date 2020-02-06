#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter10/1002-reload.py
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
import sys
import os
sys.path.append(os.path.expanduser('~/python'))
import hello #← Hello, world!
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
import importlib
hello = importlib.reload(hello) #← Hello, world!  （2つめ）
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
