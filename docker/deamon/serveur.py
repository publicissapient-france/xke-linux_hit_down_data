


import http.server

from lib.Handler import *


class MyHTTPServer(http.server.HTTPServer):
    def __init__(self, *args, **kw):
        http.server.HTTPServer.__init__(self, *args, **kw)
        self.context = Context(0, State.toWelcomeMessage)


if __name__ == "__main__":
    server = MyHTTPServer(('', 80), Handler)
    server.context = Context(0, State.toWelcomeMessage)
    logThat("INFO", server.context.next)
    server.serve_forever()
