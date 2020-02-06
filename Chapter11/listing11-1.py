#ファイル名 Chapter11/listing11-1.py （somescript.py）
import sys
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print('単語数：', wordcount)
