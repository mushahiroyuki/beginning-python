#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter09/0906-sequence.py
def check_index(key):
#@#     Is the given key an acceptable index?
#@#     To be acceptable, the key should be a non-negative integer. If it
#@#     is not an integer, a TypeError is raised; if it is negative, an
#@#     IndexError is raised (since the sequence is of infinite length).
    """
    与えられたキーはインデックスとして適切か（非負の整数かどうか）をチェックする。
    整数でなければTypeErrorを、負ならばIndexErrorを生成（シーケンスの長さが無限なので）。
    """
    if not isinstance(key, int): raise TypeError #← keyが整数でなければ「型のエラー」
    if key < 0: raise IndexError #← keyが負数ならば「インデックスエラー」
   
class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        """
        等差数列の初期化
        start   - 初項（数列の最初の項の値）
        step    - 公差（2つの隣り合った値の差）
        changed - ユーザーによって変更された値のインデックスを記憶
        """
        self.start = start #← 初項の値を保存
        self.step = step #← 公差を保存
        self.changed = {} #← 変更された項は最初はなし
    def __getitem__(self, key):
        """
        等差数列から値を取得する
        """
        check_index(key) #←インデックスをチェック。問題があれば例外がraiseされる
        try: return self.changed[key] #← 変更されていれば、値を返す
        except KeyError: #← 変更されていなければ...
            return self.start + key * self.step   #← 値を計算する
    def __setitem__(self, key, value):
        """
        等差数列内の項を変更する
        """
        check_index(key)
        self.changed[key] = value #← 変更された項の値を記憶
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#実行

#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
s = ArithmeticSequence(1, 2)
print(s[4]) #← 9
s[4] = 2
print(s[4]) #← 2
print(s[5]) #← 11
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list3)  # ←この行は無視してください。本文に引用するためのものです。
del s[4] #← AttributeError: __delitem__
s["four"] #← TypeError   （この行を試すには上の行をコメントにしてください）
s[-42]  #← IndexError （この行を試すには上の2行をコメントにしてください）
#@@range_end(list3)  # ←この行は無視してください。本文に引用するためのものです。
