from ricxappframe.xapp_frame import RMRXapp
import json
import http.server
import socketserver
import threading

from ._BaseManager import _BaseManager

class RestManager(_BaseManager):
    def __init__(self, rmr_xapp: RMRXapp):
        super().__init__(rmr_xapp)

    class DefaultHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, logger=None, **kwargs):
            self.logger = logger
            super().__init__(*args, **kwargs)

        def do_GET(self):
            headers_dict = dict(self.headers)
            self.logger.info("RestManager.do_GET:: Path: {}, Headers: {}".format(str(self.path), headers_dict))
            self.send_response(200)

        def do_POST(self):
            headers_dict = dict(self.headers)
            content_length = int(self.headers['Content-Length']) # Gets the size of data
            post_data = self.rfile.read(content_length) # Gets the data itself
            data_dict = json.loads(post_data.decode('utf-8'))
            self.logger.info("RestManager.do_POST:: Path: {}, Headers: {}, Body: {}".format(str(self.path), headers_dict, data_dict))
            self.send_response(200)

    class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
        pass

    def start_http_server(self, port: int):
        self.logger.info("RestManager.start_http_server:: Starting HTTP server on port {}".format(port))
        server_address = ('', port)

        # Factory function that returns a new DefaultHttpRequestHandler with the logger set
        def handler_factory(*args, **kwargs):
            return self.DefaultHttpRequestHandler(*args, logger=self.logger, **kwargs)

        httpd = self.ThreadedHTTPServer(server_address, handler_factory)
        
        # Start the server in a new thread
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.start()



