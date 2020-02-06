#ファイル名 Chapter14/listing14-6.py
import socket, select

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
inputs = [s]
while True:
    rs, ws, es = select.select(inputs, [], [])
    for r in rs:
        if r is s:
            c, addr = s.accept()
#@#             print('Got connection from', addr)
            print('接続受付：', addr)
            inputs.append(c)
        else:
            try:
                data = r.recv(1024)
                disconnected = not data
            except socket.error:
                disconnected = True

            if disconnected:
#@#                 print r.getpeername(), 'disconnected'
                print(r.getpeername(), '接続解除')
                inputs.remove(r)
            else:
#@#                 print data
                print(str(data, 'utf-8'))
