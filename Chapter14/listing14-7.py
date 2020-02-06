#ファイル名 Chapter14/listing14-7.py
import socket, select

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

fdmap = {s.fileno(): s}


s.listen(5)
p = select.poll()
p.register(s)
while True:
    events = p.poll()
    for fd, event in events:
        if fd in fdmap:
            c, addr = s.accept()
#@#             print 'Got connection from', addr
            print('接続受付：', addr)
            p.register(c)
            fdmap[c.fileno()] = c
        elif event & select.POLLIN:
            data = fdmap[fd].recv(1024)
#@#             if not data: # No data -- connection closed
            if not data: # データがない -- 接続はクローズしている
#@#                 print fdmap[fd].getpeername(), 'disconnected'
                print(fdmap[fd].getpeername(), '接続解除')
                p.unregister(fd)
                del fdmap[fd]
            else:
#@#                 print data
                print(str(data, 'utf-8'))
