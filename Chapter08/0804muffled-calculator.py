#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter08/0804muffled-calculator.py
class MuffledCalculator: #←「マフラー」機能付き計算機
    muffled = False #←デフォルトではマフラー機能は無効
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError: 
            if self.muffled:
                print('ゼロによる除算は不正な演算です')
            else:
                raise
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#実行
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
mc = MuffledCalculator()
print(mc.calc("5/2")) #←2.5
mc.muffled = True
print(mc.calc("5/0")) #←「ゼロによる除算は不正な演算です」に続いて「None」が表示される
mc.muffled = False
print(mc.calc("5/0")) #←例外発生（ZeroDivisionError）
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
