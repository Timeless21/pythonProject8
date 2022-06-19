from http.server import HTTPServer, CGIHTTPRequestHandler

address = ("", 4000)
httpd = HTTPServer(address, CGIHTTPRequestHandler)
httpd.serve_forever()
httpd.shutdown()
