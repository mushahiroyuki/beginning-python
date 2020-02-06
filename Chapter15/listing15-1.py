#ファイル名 Chapter15/listing15-1.py
import requests
import re
p = re.compile('<a href="(/jobs/\\d+)/">(.*?)</a>')
text = requests.get("https://www.python.org/jobs").text
for url, name in p.findall(text):
    print(f'{name} ({url})')
