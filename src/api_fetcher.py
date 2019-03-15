import json, requests, time

_URL = "http://192.168.0.16:8545/"
_HEADERS = {'content-type': 'application/json'}

'''Sends request to RPC API of the service specified by url'''
def send_request(method, url=_URL, params=[]):
	payload = {
		"method":method,
		"params":params,
		"id":1,
		"jsonrpc":"2.0"
	}
	return requests.post(url, data=json.dumps(payload), headers=_HEADERS).json()
