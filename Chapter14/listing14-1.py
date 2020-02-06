#ファイル名 Chapter14/listing14-1.py
import socket

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
#@# print('Got connection from', addr)
    print('接続受付：', addr)
#@#     c.send('Thank you for connecting')
    c.send(bytes('接続ありがとうございます', 'utf-8'))
    c.close()
