import os
import time


class ResponseGenerator:
    EXTENSION_TO_MIME = {
        'html': 'text/html',
        'txt': 'text/plain',
        'png': 'image/png',
        'jpg': 'image/jpg',
        'jpeg': 'image/jpeg',
        'gif': 'image/gif',
        'css': 'text/css',
        'js': 'text/javascript'
    }

    def __init__(self, client, status_code, file_path, host_name, port):
        self.client = client
        self.status_code = status_code
        self.file_path = file_path
        self.host_name = host_name
        self.port = port

    def generate_response(self):
        response = "HTTP/1.0 {}\r\n".format(self.status_code)
        response += "Date: {}\r\n".format(time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime()))
        response += "Server: Chokotra/0.1\r\n"

        if self.status_code.startswith('3'):
            response += "Location: http://{}:{}{}\r\n".format(self.host_name, self.port, self.file_path)
            response += "\r\n"
        else:
            response += "Content-Type: {}\r\n".format(self.content_type())
            response += "\r\n"

            content = self.read_file()
            response += content
        self.client.send(response.encode())

    def read_file(self):
        with open(self.file_path, 'r') as file:
            content = file.read()
        return content

    def content_type(self):
        ext = os.path.splitext(self.file_path)[1].lstrip('.')
        return self.EXTENSION_TO_MIME.get(ext, 'text/html')
