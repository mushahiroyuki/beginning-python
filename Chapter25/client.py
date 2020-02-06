#ファイル名 client.py（listing25-3.py）
from xmlrpc.client import ServerProxy, Fault
from cmd import Cmd
from random import choice
from string import ascii_lowercase
from server import Node, UNHANDLED
from threading import Thread
from time import sleep
import sys

HEAD_START = 0.1 # 秒
SECRET_LENGTH = 100

def random_string(length):
    """
    指定長のランダム文字列を返す
    """
    chars = []
    letters = ascii_lowercase[:26]
    while length > 0:
        length -= 1
        chars.append(choice(letters))
    return ''.join(chars)

class Client(Cmd):
    """
    Nodeクラスに対するシンプルなテキスト型インタフェース
    """

    prompt = '> '

    def __init__(self, url, dirname, urlfile):
        """
        URL, ディレクトリ名、URLファイルを設定し、
        ノードサーバーを別スレッドで起動する
        """
        Cmd.__init__(self)
        self.secret = random_string(SECRET_LENGTH)
        n = Node(url, dirname, self.secret)
        t = Thread(target=n._start) 
        t.setDaemon(1)
        t.start()
        # サーバーに起動をかける
        sleep(HEAD_START)
        self.server = ServerProxy(url)
        for line in open(urlfile):
            line = line.strip()
            self.server.hello(line)

    def do_fetch(self, arg):
        "サーバーのfetchメソッドを呼び出す"
        try:
            self.server.fetch(arg, self.secret)
        except Fault as f:
            if f.faultCode != UNHANDLED: raise
            print("ファイルが見つかりませんでした -", arg)

    def do_exit(self, arg):
        "プログラムを終了させる"
        print()
        sys.exit()
    do_EOF = do_exit # End-Of-Fileは「exit」と同じ働き

def main():
    urlfile, directory, url = sys.argv[1:]
    client = Client(url, directory, urlfile)
    client.cmdloop()

if __name__ == '__main__': main()
