import os
import socket
import threading
from dotenv import load_dotenv
from server.server_thread import ServerThread

load_dotenv()


class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        port = int(os.getenv('PORT', 8001))
        self.server.bind(('', port))
        self.server.listen()

    def run(self):
        while True:
            client, addr = self.server.accept()
            thread = threading.Thread(target=ServerThread(client).process_request)
            thread.start()
