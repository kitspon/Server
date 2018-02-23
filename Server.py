import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
handler = http.server.SimpleHTTPRequestHandler
httpd = HTTPServer(("",8000), handler)
print("localhost:8000")
httpd.serve_forever()

