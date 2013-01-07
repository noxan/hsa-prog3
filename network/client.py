import socket


class Client(object):
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
        self.connected = True
