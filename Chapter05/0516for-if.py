# ファイル名 Chapter05/0516for-if.py
girls = ['かなこ', 'ゆう', 'ひでみ']
boys = ['ゆうへい', 'ひろし', 'かずき']
couples = [b + '+' + g for b in boys for g in girls if b[0] == g[0]]
print(couples)

