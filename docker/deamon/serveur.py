import http.server
from lib.Context import *
from lib.State import *
from lib.Handler import *

class S(http.server.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()



    def do_POST(self):
        # Doesn't do anything with posted data
        print("incomming http: ", self.path)

        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        print (post_data)  # <-- Print post data
        self._set_headers()
        self.wfile.write(b"<html><body><h1>POST!</h1></body></html>")


def run(server_class=http.server.HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print
    'Starting httpd...'
    httpd.serve_forever()

class MyHTTPServer(http.server.HTTPServer):

    def __init__(self, *args, **kw):
        http.server.HTTPServer.__init__(self, *args, **kw)
        self.context = Context(0, State.toWelcomeMessage)


if __name__ == "__main__":

    server = MyHTTPServer(('', 80), Handler)
    server.serve_forever()





