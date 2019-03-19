import json, requests, time

_URL = "http://192.168.0.16:8545/"
_HEADERS = {'content-type': 'application/json'}

def send_request(method, url=None, params=[]):
	payload = {
		'method':method,
		'params':params,
		'id':1,
		'jsonrpc':'2.0'
	}
	return requests.post(
		_URL if url is None else url,
		data=json.dumps(payload),
		headers=_HEADERS
	).json()
