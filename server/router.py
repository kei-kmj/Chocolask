from app.controller import Controller


class Router:
    def __init__(self, client, path, method, body):
        self.client = client
        self.path = path
        self.method = method
        self.body = body

    def send_response(self):
        if self.method == 'GET':
            Controller(self.client, self.path, self.method, self.body).index()
        elif self.method == 'POST':
            Controller(self.client, self.path, self.method, self.body).create()
