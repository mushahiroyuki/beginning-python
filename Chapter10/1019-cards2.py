#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
# ファイル名 Chapter10/1019-cardss.py
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。
from random import shuffle
from pprint import pprint

values = list(range(1, 11)) + 'J Q K'.split()
suits = '♢ ♧ ♡ ♤'.split()
deck = [f'{s} {v}' for v in values for s in suits]
#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
shuffle(deck)
while deck: input(deck.pop())
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。

