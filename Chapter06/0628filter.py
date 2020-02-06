#ファイル名 Chapter06/0628filter.py
def func(x):
    return x.isalnum()  # アルファベットか数字ならばTrueを返す

seq = ["foo", "x41", "?!", "***"]
print(list(filter(func, seq)))
