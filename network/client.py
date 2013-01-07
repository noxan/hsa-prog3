import socket


class Client(object):
    def __init__(self, host="localhost", port=10857):
        super(Client, self).__init__()
        self.host = host
        self.port = port

    def connect(self):
        self._socket = socket.socket()
        self._socket.connect((self.host, self.port))
