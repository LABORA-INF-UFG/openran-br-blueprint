from ricxappframe.xapp_frame import RMRXapp
import json
import http.server
import socketserver
import threading
from mdclogpy import Level
from mdclogpy import Logger

from ._BaseManager import _BaseManager

class RestManager(_BaseManager):
    def __init__(self, rmr_xapp: RMRXapp):
        super().__init__(rmr_xapp)
        self.logger = Logger(name=__name__)
        self.logger.set_level(Level.DEBUG)

    class DefaultHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, rmr_xapp:RMRXapp=None, logger=None, **kwargs):
            self._rmr_xapp = rmr_xapp
            self.logger = logger
            super().__init__(*args, **kwargs)
        
        def log_message(self, format, *args): # Overridden to prevent unnecessary logging
            pass

        def do_GET(self):
            headers_dict = dict(self.headers)
            self.logger.info("RestManager.do_GET:: Path: {}, Headers: {}".format(str(self.path), headers_dict))
            if self.path == "/ric/v1/config":
                self.logger.info("RestManager.do_GET:: Responding with config data")

                # Send the headers
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()

                # Write the response body
                response = {
                    "metadata":{
                        "xappName": self._rmr_xapp.config.get("name"),
                        "configType": "json"
                    },
                    "config": self._rmr_xapp.config
                }
                self.wfile.write(json.dumps(self._rmr_xapp.config).encode())

        def do_POST(self):
            headers_dict = dict(self.headers)
            content_length = int(self.headers['Content-Length']) # Gets the size of data
            post_data = self.rfile.read(content_length) # Gets the data itself
            data_dict = json.loads(post_data.decode('utf-8'))
            self.logger.info("RestManager.do_POST:: Path: {}, Headers: {}, Body: {}".format(str(self.path), headers_dict, data_dict))
            self.send_response(200) # Reply OK

    class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
        pass

    def start_http_server(self, port: int):
        server_address = ("", port)
        self.logger.info("RestManager.start_http_server:: Starting HTTP server on port {}".format(port))

        # Factory function that returns a new DefaultHttpRequestHandler with the logger set
        def handler_factory(*args, **kwargs):
            return self.DefaultHttpRequestHandler(*args, rmr_xapp=self._rmr_xapp, logger=self.logger, **kwargs)

        self.httpd = self.ThreadedHTTPServer(server_address, handler_factory)
        
        # Start the server in a new thread
        self.server_thread = threading.Thread(target=self.httpd.serve_forever)
        self.server_thread.start()
    
    def stop_server(self):
        self.logger.info("RestManager.stop_server:: Stopping HTTP server")
        self.httpd.shutdown()
        self.httpd.server_close()