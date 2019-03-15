import json, requests, time

_URL = "http://192.168.0.16:8545/"
_HEADERS = {'content-type': 'application/json'}

'''Sends request to RPC API of the service specified by url'''
def send_request(url, method, params=[]):
	payload = {
		"method":method,
		"params":params,
		"id":1,
		"jsonrpc":"2.0"
	}
	return requests.post(url, data=json.dumps(payload), headers=headers).json()

'''Sends request to RPC API to the service at default IP'''
def send_request(method, params=[]):
	send_request(_URL, method, params)


response = sendRequest("http://172.18.0.4:8545/", "admin_peers")
