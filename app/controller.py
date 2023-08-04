import os
import json
from pathlib import Path
from dotenv import load_dotenv
from server.response_generator import ResponseGenerator

load_dotenv()


class Controller:
    HOST_NAME = os.getenv('HOST_NAME')
    PORT = os.getenv('PORT')
    TODOS_ROOT = os.getenv('TODOS_ROOT', None)

    def __init__(self, request_handler, path, method, body=None):
        self.request_handler = request_handler
        self.path = path
        self.method = method
        self.body = body

    def generate_response(self, status_code, path):
        response_generator = ResponseGenerator(self.request_handler, status_code, path, self.HOST_NAME, self.PORT)
        response_generator.generate_response()

    def index(self):
        if self.path.endswith('/'):
            self.path += 'index.html'

        file_path = Path(f"{self.TODOS_ROOT}{self.path}")
        if file_path.is_dir():
            self.path += '/index.html'
            self.generate_response('301 Moved Permanently', f"{self.TODOS_ROOT}{self.path}")
        elif file_path.is_file():
            self.generate_response('200 OK', f"{self.TODOS_ROOT}{self.path}")
        else:
            self.generate_response('404 Not Found', f"{self.TODOS_ROOT}/404.html")

    def create(self):
        new_todo = json.loads(self.body)
        todos_file_path = f"{self.TODOS_ROOT}/todos.json"

        if Path(todos_file_path).is_file():
            with open(todos_file_path, 'r') as file:
                todos = json.load(file)
        else:
            todos = []

        todos.append(new_todo)
        json_indent = int(os.getenv('JSON_INDENT', 4))
        with open(todos_file_path, 'w') as file:
            json.dump(todos, file, indent=json_indent)

        self.generate_response('200 OK', f"{self.TODOS_ROOT}/index.html")
