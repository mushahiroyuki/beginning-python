#ファイル名 Chapter06/0620story.py
def story(**kwds):
    return '昔むかし、あるところに{name}という名前の{job}が存在していました。'.format_map(kwds)

def power(x, y, *others):
    if others:
        print('余分な引数を受け取りました:', others)
    return pow(x, y)

def interval(start, stop=None, step=1):
    '模擬的range()、ただしステップ（step）> 0の場合'
    if stop is None:  # stopが指定されていない
        start, stop = 0, start  # 引数を入れ替え。stopを指定された値に
    result = []
    i = start  # startのインデックスから始める
    while i < stop:  # インデックスがstopに達するまで...
        result.append(i)  # result（結果）にインデックスを追加
        i += step  # インデックスをステップ（step > 0）だけ増加
    return result

# 実行
print(story(job='王様', name='ガンビー'))
print(story(name='サー・ロビン', job='勇敢な騎士')) # モンティー・パイソンより

print('-'*20, 1) # 区切り線 1
params = {'job': '言語', 'name': 'Python'}
print(story(**params))
del params['job']
print(story(job='天才的な閃きを授けるツール', **params))

print('-'*20, 2) # 区切り線 2
print(power(2, 3))
print(power(3, 2))
print(power(y=3, x=2))

print('-'*20, 3) # 区切り線 3
params = (5,) * 2
print(power(*params))
print(power(3, 3, 'Hello, world'))

print('-'*20, 4) # 区切り線 4
print(interval(10))
print(interval(1, 5))
print(interval(3, 12, 4))
print(power(*interval(3, 7)))
