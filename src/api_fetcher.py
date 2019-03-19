import json, requests, time

_URL = "http://192.168.0.16:8545/"
_HEADERS = {'content-type': 'application/json'}

'''Contains send_request that sends request'''
class SendRequest():
	
	'''If url/headers not specified uses default values'''
	def __init__(self, url=None, headers=None):
		self._URL = _URL if url is None else url
		self._HEADERS = _HEADERS if headers is None else headers

	'''Sends request to RPC API of the service specified by url'''
	def send_request(self, method, url=None, params=[]):
		payload = {
			'method':method,
			'params':params,
			'id':1,
			'jsonrpc':'2.0'
		}
		return requests.post(
			self._URL if url is None else url,
			data=json.dumps(payload),
			headers=self._HEADERS
		).json()
