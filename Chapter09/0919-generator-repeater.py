#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter09/0919-generator-repeater.py
def repeater(value):
    while True:
        new = (yield value) #← 実行を再開するときに値を受け取る。括弧で囲む
        if new is not None: value = new #← 値がNoneでなければ次回その値を渡す。Noneだと次回も前と同じ値を渡す
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
r = repeater(42) #← ジェネレータが戻されるのでそれをrに代入
print(next(r)) #← 42 関数nextの引数にジェネレータを指定して「次」の値をもらう
print(next(r)) #← 42 値は変わらない 
print(r.send("メッセージ１")) #← メッセージ１
print(next(r)) #← メッセージ１
print(r.send("メッセージ２")) #← メッセージ２
print(next(r)) #← メッセージ２
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。
