import socket
import threading


class Connection(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client

    def run(self):
        self.client.send('Hello World')
        self.client.close()

class Server(object):
    def __init__(self, host='0.0.0.0', port=10857):
        self.running = False
        self.host = host
        self.port = port

    def start(self):
        if self.running:
            raise Exception("Server already running.")
        self.running = True
        self._socket = socket.socket()
        self._socket.bind((self.host, self.port))
        self._connections = []
        self.run()

    def run(self):
        self._socket.listen(5)
        while self.running:
            client, addr = self._socket.accept()
            print "Got connection from %s." % str(addr)
            connection = Connection(client)
            connection.start()
            self._connections.append(connection)
            self.clean()

    def clean(self):
        for connection in self._connections:
            if not connection.isAlive():
                self._connections.remove(connection)
                connection.join(3)

if '__main__' == __name__:
    server = Server()
    server.start()
