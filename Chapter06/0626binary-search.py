#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter06/0626binary-search.py
def search(sequence, number, lower, upper): # numberを探す
    print(lower, upper) # 現在の下限と上限を出力
    if lower == upper: # 上限と下限が同じなら
         assert number == sequence[upper] # 同じ数が見つかったと仮定
         return upper 
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

range = range(50)
print (search(range, 22, 0, 50), "が見つかりました");
