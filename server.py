import http.server
import socketserver
import threading

PORT = 80
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((, PORT), handler) as httpd:
    print(Serving HTTP at port, PORT)
    try:
        threading.Thread(target=httpd.serve_forever())
    except KeyboardInterrupt:
        httpd.shutdown()

