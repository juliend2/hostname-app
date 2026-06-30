import os
from http.server import BaseHTTPRequestHandler, HTTPServer
 
HOSTNAME = os.environ.get("HOSTNAME", "unknown")
 
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(f"{HOSTNAME}\n".encode())
 
    def log_message(self, format, *args):
        pass  # silence access logs
 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    HTTPServer(("", port), Handler).serve_forever()
 

