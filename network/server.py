import socket

s = socket.socket()
host = socket.gethostname()
port = 10857
s.bind((host, port))

s.listen(5)
while True:
    connection, addr = s.accept()
    print 'Got connection from %s' % str(addr)
    connection.send('Hello World')
    connection.close()
