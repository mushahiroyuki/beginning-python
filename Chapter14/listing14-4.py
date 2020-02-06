#ファイル名 Chapter14/listing14-4.py
from socketserver import TCPServer, ForkingMixIn, StreamRequestHandler

class Server(ForkingMixIn, TCPServer): pass

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
#@#         print('Got connection from', addr)
        print('接続受付：', addr)
#@#         self.wfile.write('Thank you for connecting')
        self.wfile.write(bytes('接続ありがとうございます', 'utf-8'))

server = Server(('', 1234), Handler)
server.serve_forever()
