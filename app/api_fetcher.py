import json, requests, socket

_URL = "http://node:8545/"
_HEADERS = {'content-type': 'application/json'}

def send_request(method, params=[], url=_URL):
	payload = {
		'method':method,
		'params':params,
		'id':1,
		'jsonrpc':'2.0'
	}
	return requests.post(
		url,
		data=json.dumps(payload),
		headers=_HEADERS
	)

def register_ips():
	ips = []
	while len(ips) < 2:
		ip = socket.gethostbyname('tasks.node')
		if ip not in ips:
			ips.append(ip)
	return ips

def register_nodes(ips):
	nodes = list()
	for ip in ips:
		node = send_request('admin_nodeInfo', [], 'http://' + ip + ':8545/').json()['result']['enode']
		if node not in nodes: nodes.append(node)
	return nodes

def setup_peers():
	ips = register_ips()
	nodes = register_nodes(ips)
	for i in range(len(nodes)):
		success = send_request('admin_addPeer', [nodes[i].replace('127.0.0.1', ips[i])])
		print(success.json())
	return nodes

def start_mining():
	ips = register_ips()
	responses = []
	for ip in ips:
		res = send_request('miner_start', [1], 'http://' + ip + ':8545/').json()
		responses.append(res)
	return responses

# {
# "jsonrpc":"2.0",
# "id":1,
# "result":{
# 	"id":"c3af701a968e5e607cb5c7665d0f2decb4eeeb433aaaea012930ba0b469d8500",
# 	"name":"Geth/v1.8.23-stable-c9427004/linux-amd64/go1.11.5",
# 	"enode":"enode://c800980f86316f5eed90b6dc841b27c93d287b74550b7f671aa2dd66082908738cf59fd94e10ab9c6836d85b031ea7e200886c667cdb118d1f0b53e4f1e05bf1@127.0.0.1:30303",
# 	"enr":"0xf896b840fb47b4050aa18b5d39ac09b71a83e413c2eae254fe36e911c153f973efeda4225e96796574817f0bec5c9a4aa1e532d77f9af5ccde74a8861aa270d94621a74d0183636170c6c5836574683f826964827634826970847f00000189736563703235366b31a103c800980f86316f5eed90b6dc841b27c93d287b74550b7f671aa2dd66082908738374637082765f8375647082765f",
# 	"ip":"127.0.0.1",
# 	"ports":{
# 		"discovery":30303,
# 		"listener":30303
# 	},
# 	"listenAddr":"[::]:30303",
# 	"protocols":{
# 		"eth":{"network":215037,"difficulty":131072,"genesis":"0xae9394e18d5e7e976599209ef7ed31c8e9ed7712bb177db7b1ce0ced27ceb1fd","config":{"chainId":215037,"homesteadBlock":0,"eip150Hash":"0x0000000000000000000000000000000000000000000000000000000000000000","eip155Block":0,"eip158Block":0},"head":"0xae9394e18d5e7e976599209ef7ed31c8e9ed7712bb177db7b1ce0ced27ceb1fd"}}
# 	}
# }
