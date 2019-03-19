class QuoteResource():
    
    def on_get(self, req, resp):
        quote = {
            'quote': "I've always been more interested in the future than the past.",
            'author': 'Grace Hopper'
        }
        resp.media = quote