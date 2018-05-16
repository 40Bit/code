#!/user/bin/env python3

import SimpleHTTPServer
import SocketServer
from urlparse import urlparse
from BaseHTTPServer import BaseHTTPRequestHandler

PORT = 9045

# Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        query = urlparse(self.path).query
        print(query)
        query_components = dict(qc.split("=") for qc in query.split("&"))

        self.wfile.write('x value = ' + query_components['x'])
#      if query_components['defaultWelcome'] == 'true':
#          print('welcome!')
#          return
        return
    

httpd = SocketServer.TCPServer(("", PORT), MyHandler)

print(PORT)
httpd.serve_forever()
