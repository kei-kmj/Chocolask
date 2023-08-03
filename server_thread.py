from router import Router


class ServerThread:
    def __init__(self, client_socket):
        self.client_socket = client_socket
        self.path = None
        self.method = None
        self.body = None

    def process_request(self):
        self.recv()
        response_generator = Router(self.client_socket, self.path, self.method, self.body)
        response_generator.send_response()
        self.close()

    def recv(self):
        data = self.client_socket.recv(4096).decode('utf-8')

    # Separate the headers from the body
        headers_raw, body = data.split("\r\n\r\n", 1)
        headers_lines = headers_raw.split("\r\n")

    # Parse the request line
        request_line = headers_lines[0]
        self.method, self.path, _ = request_line.split()

    # Parse the headers
        headers = {}
        for line in headers_lines[1:]:
            key, value = line.split(": ", 1)
            headers[key] = value

    # Parse the body
        if self.method == "POST":
            content_length = int(headers.get("Content-Length", 0))
            self.body = body[:content_length]
        else:
            self.body = None

    def close(self):
        self.client_socket.close()
