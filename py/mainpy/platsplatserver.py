#!/user/bin/env python3

import SimpleHTTPServer
import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler

PORT = 7528 

# Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write('{"status": "saved"}')
        return
    

httpd = SocketServer.TCPServer(("", PORT), MyHandler)

print "serving at port", PORT
httpd.serve_forever()
