class RequestNode():
    '''Needs an instance of SendRequest'''
    def __init__(self, send_request):
        self.send_request = send_request.send_request

    def on_get(self, req, resp):
        resp.media = self.send_request(
            method='admin_peers'
        )
