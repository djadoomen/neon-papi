import json, requests, time

_URL = ""
_HEADERS = {'content-type': 'application/json'}

'''Sends request to RPC API of the node specified by url'''
def sendRequest(url, method, params=[]):
	payload = {
		"method":method,
		"params":params,
		"id":1,
		"jsonrpc":"2.0"
	}
	return requests.post(url, data=json.dumps(payload), headers=headers).json()


response = sendRequest("http://172.18.0.4:8545/", "admin_peers")

print("# ----- API FETCHER ----- #")
print(response["result"])

