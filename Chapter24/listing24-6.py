#ファイル名 Chapter24/listing24-6.py
from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore

PORT = 5005
NAME = 'TestChat'

class EndSession(Exception): pass

class CommandHandler:
    """
    標準ライブラリのcmd.Cmdに似たコマンドハンドラ
    """

    def unknown(self, session, cmd):
        '不明なコマンドへの応答'
#@#     session.push('不明なコマンド: {}s\r\n'.format(cmd))
        session.push('不明なコマンド: {}\r\n'.format(cmd).encode())

    def handle(self, session, line):
        '所定のセッションから受け取った1行を処理する'
        if not line.strip(): return
        # コマンドを分離する
        parts = line.split(' ', 1)
        cmd = parts[0]
        try: line = parts[1].strip()
        except IndexError: line = ''
        # ハンドラの取得を試みる
        meth = getattr(self, 'do_' + cmd, None)
        try:
            # 呼び出し可能と仮定して呼び出す
            meth(session, line)
        except TypeError:
            # 呼び出し可能でなかった場合、その不明なコマンドに応答する
            self.unknown(session, cmd)

class Room(CommandHandler):
    """
    1人以上のユーザー（セッション）が入れる汎用の環境
    基本コマンドの処理とブロードキャストを行う。
    """

    def __init__(self, server):
        self.server = server
        self.sessions = []

    def add(self, session):
        'セッション（ユーザー）が入室した'
        self.sessions.append(session)

    def remove(self, session):
        'セッション（ユーザー）が退室した'
        self.sessions.remove(session)

    def broadcast(self, line):
        '室内の全セッションに1行を送信する'
        for session in self.sessions:
#@#          session.push(line)
            session.push(line.encode())

    def do_logout(self, session, line):
        'logoutコマンドに応答する'
        raise EndSession

class LoginRoom(Room):
    """
    接続したばかりの単独の人用に定めた部屋
    """

    def add(self, session):
        Room.add(self, session)
        # ユーザーが入室したときに挨拶をする
        self.broadcast('{}にようこそ\r\n'.format(self.server.name))

    def unknown(self, session, cmd):
        # 不明なコマンド（login、logout以外すべて）の場合、
        # ログインを促す
#@#      session.push('ログインしてください\n「login <名前>」と入力"\r\n')
        session.push('ログインしてください\n「login <名前>」と入力\r\n'.encode())

    def do_login(self, session, line):
        name = line.strip()
        # ユーザーが名前を入力したことを確認する
        if not name:
#@#          session.push('名前を入力してください\r\n')
            session.push('名前を入力してください\r\n'.encode())
        # 入力された名前が使用中でないことを確認する
        elif name in self.server.users:
#@#          session.push('その名前 "{}" は使用されています\r\n'.format(name))
            session.push('その名前 "{}" は使用されています\r\n'.format(name).encode())
#@#          session.push('やり直してください。\r\n')
            session.push('やり直してください。\r\n'.encode())
        else:
            # 名前に問題がないので、それをセッションに保存し、
            # ユーザーをメインルームに移動させる
            session.name = name
            session.enter(self.server.main_room)

class ChatRoom(Room):
    """
    室内の他の人とチャットできる複数のユーザー用の部屋
    """

    def add(self, session):
        # 新たなユーザーが入室したことを全員に通知する
        self.broadcast(session.name + 'が入室しました。\r\n')
        self.server.users[session.name] = session
        super().add(session)

    def remove(self, session):
        Room.remove(self, session)
        # ユーザーが退室したことを全員に通知する
        self.broadcast(session.name + 'が退室しました。\r\n')

    def do_say(self, session, line):
        self.broadcast(session.name + ': ' + line + '\r\n')

    def do_look(self, session, line):
        'lookコマンドの処理（部屋に誰がいるかを見るのに使用）'
#@#      session.push('以下の人がこの部屋にいます。\r\n')
        session.push('以下の人がこの部屋にいます。\r\n'.encode())
        for other in self.sessions:
#@#          session.push(other.name + '\r\n')
            session.push((other.name + '\r\n').encode())

    def do_who(self, session, line):
        'whoコマンドの処理（誰がログインしているか見るのに使用）'
#@#      session.push('以下の人がログインしています。\r\n')
        session.push('以下の人がログインしています。\r\n'.encode())
        for name in self.server.users:
#@#          session.push(name + '\r\n')
            session.push((name + '\r\n').encode())

class LogoutRoom(Room):
    """
    ユーザー1人用の単純な部屋。唯一の目的はユーザーの名前をサーバーから削除すること。
    """

    def add(self, session):
        # セッション（ユーザー）がLogoutRoomに入ったときに、そのセッションを削除する
        try: del self.server.users[session.name]
        except KeyError: pass

class ChatSession(async_chat):
    """
    単一のセッション。単一のユーザーとの通信を扱う。
    """

    def __init__(self, server, sock):
        super().__init__(sock)
        self.server = server
#@#      self.set_terminator("\r\n")
        self.set_terminator(b"\r\n")
        self.data = []
        self.name = None
        # すべてのセッションは個別のLoginRoomで始まる。
        self.enter(LoginRoom(server))

    def enter(self, room):
        # 現在の部屋からselfを削除し、
        # selfを次の部屋に加える...
        try: cur = self.room
        except AttributeError: pass
        else: cur.remove(self)
        self.room = room
        room.add(self)

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
#@#      line = ''.join(self.data)
        line = b''.join(self.data)
        self.data = []
#@#      try: self.room.handle(self, line)
        try: self.room.handle(self, line.decode())
        except EndSession: self.handle_close()

    def handle_close(self):
        async_chat.handle_close(self)
        self.enter(LogoutRoom(self.server))

class ChatServer(dispatcher):
    """
    単一の部屋を備えたチャットサーバー
    """

    def __init__(self, port, name):
        super().__init__()
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.name = name
        self.users = {}
        self.main_room = ChatRoom(self)

    def handle_accept(self):
        conn, addr = self.accept()
        ChatSession(self, conn)

if __name__ == '__main__':
    s = ChatServer(PORT, NAME)
    try: asyncore.loop()
    except KeyboardInterrupt: print()
