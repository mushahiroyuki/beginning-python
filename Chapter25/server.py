#ファイル名 server.py（listing25-2.py）
from xmlrpc.client import ServerProxy, Fault
from os.path import join, abspath, isfile
from xmlrpc.server import SimpleXMLRPCServer
from urllib.parse import urlparse
import sys

SimpleXMLRPCServer.allow_reuse_address = 1

MAX_HISTORY_LENGTH = 6

UNHANDLED     = 100
ACCESS_DENIED = 200

class UnhandledQuery(Fault): 
    """
    クエリを処理できなかったことを示す例外
    """
    def __init__(self, message="クエリを処理できませんでした"):
        super().__init__(UNHANDLED, message)

class AccessDenied(Fault):
    """
    ユーザーがアクセス権限を持たないリソースに
    アクセスを試みた場合に送出される例外
    """
    def __init__(self, message="アクセスが拒否されました"):
        super().__init__(ACCESS_DENIED, message)

def inside(dir, name):
    """
    指定ファイルが指定ディレクトリ内にあるかどうか検査する
    """
    dir = abspath(dir)
    name = abspath(name)
    return name.startswith(join(dir, ''))

def get_port(url):
    """
    URLからポート番号を切り出す
    """
    name = urlparse(url)[1]
    parts = name.split(':')
    return int(parts[-1])

class Node:
    """
    ピアツーピア型ネットワークのノード
    """
    def __init__(self, url, dirname, secret):
        self.url = url
        self.dirname = dirname
        self.secret = secret
        self.known = set()

    def query(self, query, history=[]):
        """
        ファイルについてのクエリを実行し、場合に応じて既知のノードにも支援を求める。
        ファイル（の内容）を文字列として返す。
        """
        try:
            return self._handle(query)
        except UnhandledQuery:
            history = history + [self.url]
            if len(history) >= MAX_HISTORY_LENGTH: raise
            return self._broadcast(query, history)

    def hello(self, other):
        """
        他のノードにこのノードを紹介する場合に使う 
        """
        self.known.add(other)
        return 0

    def fetch(self, query, secret):
        """
        このノードにファイルの探索とダウンロードをさせる場合に使う
        """
        if secret != self.secret: raise AccessDenied
        result = self.query(query)
        f = open(join(self.dirname, query), 'w')
        f.write(result)
        f.close()
        return 0

    def _start(self):
        """
        XML-RPCサーバーを起動する（内部的に使用）
        """
        s = SimpleXMLRPCServer(("", get_port(self.url)), logRequests=False)
        s.register_instance(self)
        s.serve_forever()

    def _handle(self, query):
        """
        クエリを処理する（内部的に使用）
        """
        dir = self.dirname
        name = join(dir, query)
        if not isfile(name): raise UnhandledQuery
        if not inside(dir, name): raise AccessDenied
        return open(name).read()

    def _broadcast(self, query, history):
        """
        クエリを既知のノードすべてにブロードキャストする（内部的に使用）
        """
        for other in self.known.copy():
            if other in history: continue
            try:
                s = ServerProxy(other)
                return s.query(query, history)
            except Fault as f:
                if f.faultCode == UNHANDLED: pass
                else: self.known.remove(other)
            except:
                self.known.remove(other)
        raise UnhandledQuery

def main():
    url, directory, secret = sys.argv[1:]
    n = Node(url, directory, secret)
    n._start()

if __name__ == '__main__': main()
