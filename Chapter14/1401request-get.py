#@@range_begin(list1)  # ←この行は無視してください。本文に引用するためのものです。
#ファイル名 Chapter14/1401request-get.py
import requests
webpage = requests.get("https://www.python.org")
#@@range_end(list1)  # ←この行は無視してください。本文に引用するためのものです。

#@@range_begin(list2)  # ←この行は無視してください。本文に引用するためのものです。
print(f"ステータスコード={webpage.status_code}")
print(f"エンコーディング={webpage.encoding}")
print(f"コンテントのタイプ={webpage.headers['content-type']}")
print(f"コンテントの長さ={webpage.headers['Content-Length']}")

html = webpage.text #←ページのHTMLコードを代入
print(f"----- HTMLコード（先頭部分100文字）\n{html[0:100]}")

import re
pattern = re.compile(r'<a href="([^"]+)', re.MULTILINE)

match = re.search('<a href="([^"]+)" .*?>about</a>', html, re.IGNORECASE)
#← 「<a href="」に続く文字列を「"」の前まで抽出。そのあとに 「>about</a>」がある
# re.IGNORECASE は大文字小文字（case）を無視（ignore）する
print(f"\nABOUTページのURL={match.group(1)}")

match = re.search('(<body (.|\s)*</body>)', html, re.IGNORECASE)
#← 「<body」から「</body>」までの文字列を見つける。「\s」で改行文字にもマッチするようにする
print("\n----- <body>部の先頭100文字 -----");
print(f"{match.group(1)[0:100]}")

print("\n----- <body>部の最後の100文字 -----");
print(f"{match.group(1)[-100:]}")
#@@range_end(list2)  # ←この行は無視してください。本文に引用するためのものです。

