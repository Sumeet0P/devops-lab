import os
from http.server import BaseHTTPRequestHandler, HTTPServer

MESSAGE = os.getenv("APP_MESSAGE", "Hello from Docker Compose")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(MESSAGE.encode())

server = HTTPServer(("0.0.0.0", 8000), Handler)
print("Server running on port 8000")
server.serve_forever()
