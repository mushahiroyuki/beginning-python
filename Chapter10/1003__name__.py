#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter10/1003__name__.py
import hello3
sys.path.append(os.path.expanduser('~/python'))
import hello #← Hello, world!
import importlib
hello = importlib.reload(hello) #← Hello, world!  （2つめ）
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
