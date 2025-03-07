import os
import http.server
import socketserver

PORTT = 8080  # 
PATH = "." 

class ServidorHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PATH, **kwargs)

def run():
    with socketserver.TCPServer(("", PORTT), ServidorHandler) as httpd:
        print(f"Server running.")
        httpd.serve_forever()

if __name__ == "__main__":
    run()
