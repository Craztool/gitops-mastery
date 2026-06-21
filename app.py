from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        html = "<html><body><h1>Test ingress</h1></p></body></html>"
        self.wfile.write(html.encode('utf-8'))

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    print(f"Сервер запущен на порту {port}...")
    server.serve_forever()