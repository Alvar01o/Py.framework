from http.server import HTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlparse

class HTTPRequestHandler(BaseHTTPRequestHandler):
    """docstring for HTTPRequestHandler"""
    
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
  
    def do_GET(self):
        print(self.path)
        print(self.wfile)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        s="Code"
        self.wfile.write(s.encode("utf-8"))
        url = urlparse(self.path)
        print(url.geturl())
