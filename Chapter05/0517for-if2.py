# ファイル名 Chapter05/0517for-if2.py
girls = ['かなこ', 'ゆう', 'ひでみ']
boys = ['ゆうへい', 'ひろし', 'かずき']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print([b+'+'+g for b in boys for g in letterGirls[b[0]]])
