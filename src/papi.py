import falcon
from wsgiref import simple_server

from api_fetcher import send_request
from controller.quote_resource import QuoteResource

app = falcon.API()
app.add_route('/quote', QuoteResource())

if __name__ == '__main__':
	httpd = simple_server.make_server('127.0.0.1', 8000, app)
	httpd.serve_forever()