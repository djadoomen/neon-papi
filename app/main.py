from flask import Flask, request

import api_fetcher as api
import json

app = Flask(__name__)

@app.route("/")
def index():
    return api.send_request('admin_peers').text

@app.route("/send_transaction", methods=['POST'])
def sendTransaction():
    rawTransaction = json.loads(request.data)['transaction']
    return api.send_request('eth_sendRawTransaction', [rawTransaction]).text

@app.route("/balance/<account>")
def balance(account):
	return api.send_request('eth_getBalance', [account, "latest"]).text

@app.route("/peers")
def peers():
	return api.send_request('net_peerCount').text

@app.route("/info")
def info():
	return api.send_request('admin_nodeInfo').text

@app.route("/setup_peers")
def setup_peers():
	return '\n'.join(api.setup_peers())

@app.route("/ip")
def ip():
	return ' '.join(api.register_ips())

@app.route("/mine")
def mine():
	responses = api.start_mining()
	dump = []
	for res in responses:
		dump.append(json.dumps(res, indent=4))
	return '\n------------------------------\n'.join(dump)

# if __name__ == "__main__":
#     app.run(host='127.0.0.1', debug=True, port=80)
