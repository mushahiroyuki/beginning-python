# ファイル名 Chapter10/1023-template.py

import fileinput, re

field_pat = re.compile(r'\[(.+?)\]') # [...]のパターンにマッチする:

scope = {} # 変数を記憶

# re.subの引数に指定される関数
def replacement(match):  # 置換する関数の定義
    code = match.group(1)
    try:
        return str(eval(code, scope)) # フィールドが評価可能なら、評価結果を返す
    except SyntaxError:
        # さもなければ同じスコープで代入を行う ... コードをスコープ内で実行
        exec(code, scope)
        return ''  # 空文字列を返す

# すべての文を1つの文字列にする:

# (他にもいくつか方法がある; 第11章を参照)
lines = []
for line in fileinput.input():
    lines.append(line)
text = ''.join(lines)

# フィールドのパターンをすべて置き換える:
print(field_pat.sub(replacement, text)) # subは re で提供されるメソッド
