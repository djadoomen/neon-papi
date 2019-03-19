import falcon
from wsgiref import simple_server

from api_fetcher import SendRequest

from controller.request_node import RequestNode

app = falcon.API()
app.add_route('/request', RequestNode(SendRequest()))

if __name__ == '__main__':
	httpd = simple_server.make_server('127.0.0.1', 8000, app)
	httpd.serve_forever()
