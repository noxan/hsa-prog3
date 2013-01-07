import socket
import threading
import select


class Client(threading.Thread):
    def __init__(self, host="localhost", port=10857):
        super(Client, self).__init__()
        self.host = host
        self.port = port
        self.connected = False

    def connect(self):
        if self.connected:
            raise Exception("Client is already connected")
        self._socket = socket.socket()
        self._socket.connect((self.host, self.port))
        self._socket.setblocking(0)
        self.connected = True
        self.run()

    def run(self):
        while self.connected:
            ready = select.select([self._socket], [], [])
            if ready[0]:
                msg = self._socket.recv(1024)
                if msg:
                    print '"%s"' % (msg.strip())
                else:
                    self.connected = False
