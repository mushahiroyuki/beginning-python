#ファイル名 Chapter24/listing24-5.py
from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore

PORT = 5005
NAME = 'TestChat'

class ChatSession(async_chat):
    """
    サーバーと単一のユーザーとの接続を取り扱うクラス
    """
    def __init__(self, server, sock):
        # 標準的なセットアップ処理
        async_chat.__init__(self, sock)
        self.server = server
#@#      self.set_terminator("\r\n")
        self.set_terminator(b"\r\n")
        self.data = []
        # ユーザーに挨拶する
#@#      self.push('%へようこそ\r\n' % self.server.name)
        self.push(('%sへようこそ\r\n' % self.server.name).encode())

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        """
        行区切りが見つかると、1行全体を読み込んだことになる。
        その行を全員にブロードキャストする。
        """
#@#      line = ''.join(self.data)
        line = b''.join(self.data)
        self.data = []
        self.server.broadcast(line)

    def handle_close(self):
        async_chat.handle_close(self)
        self.server.disconnect(self)

class ChatServer(dispatcher):
    """
    接続を受けて個別のセッションを生成するクラス
    それらのセッションへのブロードキャストも行う。
    """
    def __init__(self, port, name):
        # 標準的なセットアップ処理
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.name = name
        self.sessions = []

    def disconnect(self, session):
        self.sessions.remove(session)

    def broadcast(self, line):
        for session in self.sessions:
#@#          session.push(line + '\r\n')
            session.push(line + b'\r\n')

    def handle_accept(self):
        conn, addr = self.accept()
        self.sessions.append(ChatSession(self, conn))

if __name__ == '__main__':
    s = ChatServer(PORT, NAME)
    try: asyncore.loop()
    except KeyboardInterrupt: print()
