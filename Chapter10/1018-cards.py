# ファイル名 Chapter10/1018-cards.py
from random import shuffle
from pprint import pprint

values = list(range(1, 11)) + 'J Q K'.split()
suits = '♢ ♧ ♡ ♤'.split()
deck = [f'{s} {v}' for v in values for s in suits]
pprint(deck)  #← カードを出力
shuffle(deck)  #← シャッフルする
print("-----------") #← 区切り線
pprint(deck) #← シャッフル後のカードを出力
