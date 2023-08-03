import socket
import threading
from server_thread import ServerThread


class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('', 8001))
        self.server.listen(5)

    def run(self):
        while True:
            client, addr = self.server.accept()
            thread = threading.Thread(target=ServerThread(client).process_request)
            thread.start()


if __name__ == '__main__':
    server = Server()
    server.run()
