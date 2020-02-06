#ファイル名 Chapter14/listing14-2.py
import socket

s = socket.socket()

host = socket.gethostname()
port = 1234

s.connect((host, port))
print(str(s.recv(1024), 'utf-8'))
#@# print(s.recv(1024))
