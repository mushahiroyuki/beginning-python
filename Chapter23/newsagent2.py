from nntplib import NNTP, decode_header
from urllib.request import urlopen
import textwrap
import re

class NewsAgent:
    """
    ニュースソースから出力先へニュース項目を配布するオブジェクト
    """

    def __init__(self):
        self.sources = []
        self.destinations = []

    def add_source(self, source):
        self.sources.append(source)

    def add_destination(self, dest):
        self.destinations.append(dest)

    def distribute(self):
        """
        全ニュースソースから全ニュース項目を取得し、それらを全出力先に配布する
        """
        items = []
        for source in self.sources:
            items.extend(source.get_items())
        for dest in self.destinations:
            dest.receive_items(items)
class NewsItem:
    """
    表題と本文のテキストからなる単純なニュース項目
    """
    def __init__(self, title, body):
        self.title = title
        self.body = body

class NNTPSource:
    """
    NNTPのグループからニュース項目を取得するニュースソース
    """
    def __init__(self, servername, group, howmany):
        self.servername = servername
        self.group = group
        self.howmany = howmany

    def get_items(self):
        server = NNTP(self.servername)
        resp, count, first, last, name = server.group(self.group)
        start = last - self.howmany + 1
        resp, overviews = server.over((start, last))
        for id, over in overviews:
            title = decode_header(over['subject'])
            resp, info = server.body(id)
            body = '\n'.join(line.decode('latin')
                             for line in info.lines) + '\n\n'
            yield NewsItem(title, body)
        server.quit()

class SimpleWebSource:
    """
    正規表現を使ってウェブページからニュース項目を取り出すニュースソース
    """
    def __init__(self, url, title_pattern, body_pattern, encoding='utf8'):
        self.url = url
        self.title_pattern = re.compile(title_pattern)
        self.body_pattern = re.compile(body_pattern)
        self.encoding = encoding

    def get_items(self):
        text = urlopen(self.url).read().decode(self.encoding)
        titles = self.title_pattern.findall(text)
        bodies = self.body_pattern.findall(text)
        for title, body in zip(titles, bodies):
            yield NewsItem(title, textwrap.fill(body) + '\n')

class PlainDestination:
    """
    すべてのニュース項目をプレーンテキストとして整形するニュース出力先
    """
    def receive_items(self, items):
        for item in items:
            print(item.title)
            print('-' * len(item.title))
            print(item.body)

class HTMLDestination:
    """
    すべてのニュース項目をHTMLとして整形するニュース出力先
    """
    def __init__(self, filename):
        self.filename = filename

    def receive_items(self, items):

        out = open(self.filename, 'w')
        print("""
        <html>
          <head>
            <meta charset="utf-8">
            <title>今日のニュース</title>
          </head>
          <body>
          <h1>今日のニュース</h1>
        """, file=out)

        print('<ul>', file=out)
        id = 0
        for item in items:
            id += 1
            print('  <li><a href="#{}">{}</a></li>'
                    .format(id, item.title), file=out)
        print('</ul>', file=out)

        id = 0
        for item in items:
            id += 1
            print('<h2><a name="{}">{}</a></h2>'
                    .format(id, item.title), file=out)
            print('<pre>{}</pre>'.format(item.body), file=out)

        print("""
          </body>
        </html>
        """, file=out)

def run_default_setup():
    """
    ニュースソースと出力先のデフォルト設定。いろいろ変更してみましょう。
    """
    agent = NewsAgent()

    # Reutersからニュースを取得するSimpleWebSource
    reuters_url = 'https://www.reuters.com/news/world'
#@# reuters_title = r'<h2><a href="[^"]*"\s*>(.*?)</a>'
    reuters_title = r'<h2 class="FeedItemHeadline_headline FeedItemHeadline_full"\s*><a href="[^"]*"\s*>(.*?)</a>'
#@# reuters_body = r'</h2><p>(.*?)</p>'
    reuters_body = r'<p class="FeedItemLede_lede"\s*>(.*?)</p>'
    reuters = SimpleWebSource(reuters_url, reuters_title, reuters_body)
    agent.add_source(reuters)

    # comp.lang.python.announceからニュースを取得するNNTPSource
#@# clpa_server = 'news.foo.bar' # Insert real server name
    clpa_server = 'nntp.aioe.org'
    clpa_group = 'comp.lang.python.announce'
#@#    clpa_group = 'alt.math.undergrad'
#@# clpa_howmany = 10
    clpa_howmany = 3
    clpa = NNTPSource(clpa_server, clpa_group, clpa_howmany)
    agent.add_source(clpa)

    # プレーンテキストの出力先とHTMLの出力先を追加する
    agent.add_destination(PlainDestination())
    agent.add_destination(HTMLDestination('news.html'))

    # ニュース項目を配布する
    agent.distribute()

if __name__ == '__main__': run_default_setup()
