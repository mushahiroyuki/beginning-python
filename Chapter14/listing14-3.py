#ファイル名 Chapter14/listing14-3.py
from socketserver import TCPServer, StreamRequestHandler

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
#@#         print('Got connection from', addr)
        print('接続受付：', addr)
#@#         self.wfile.write('Thank you for connecting')
        self.wfile.write(bytes('接続ありがとうございます', 'utf-8'))

server = TCPServer(('', 1234), Handler)
server.serve_forever()
