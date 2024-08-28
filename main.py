from http.server import HTTPServer, BaseHTTPRequestHandler

class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            # defines file as the path that the user writes in browser and reads it - "1:" is used to skip the first char, which would be forward slash
            file = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file = "File not found, sorry :/"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file, 'utf-8'))


httpd = HTTPServer(('localhost', 8400), Server)
httpd.serve_forever()