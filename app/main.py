from flask import Flask, request

import api_fetcher as api
import json

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route("/")
def index():
    return api.send_request('admin_peers').text

@app.route("/send_transaction", methods=['POST'])
def sendTransaction():
    transaction = json.loads(request.data)['transaction']
    return api.send_request('eth_sendRawTransaction', [transaction]).text

@app.route("/execute", methods=['POST'])
def execute():
    data = json.loads(request.data)
    return api.send_request(data['method'], data['params']).text

@app.route("/transaction_receipt/<transaction_hash>")
def transaction_receipt(transaction_hash):
    return api.send_request('eth_getTransactionReceipt', [transaction_hash]).text

@app.route("/transaction/<transaction_hash>")
def transaction(transaction_hash):
    return api.send_request('eth_getTransactionByHash', [transaction_hash]).text

@app.route("/block/<number>")
def block(number):
    return api.send_request('eth_getBlockByNumber', [number, True]).text

@app.route("/block_number")
def block_number():
    return api.send_request('eth_blockNumber').text

@app.route("/transaction_nonce/<account>")
def transaction_nonce(account):
    return api.send_request('eth_getTransactionCount', [account, "latest"]).text

@app.route("/pending_transactions")
def pending_transactions():
    return api.send_request('eth_pendingTransactions').text

@app.route("/balance/<account>")
def balance(account):
	return api.send_request('eth_getBalance', [account, "latest"]).text

@app.route("/peers")
def peers():
	return api.send_request('net_peerCount').text

@app.route("/setup_peers")
def setup_peers():
	return '\n'.join(api.setup_peers())

@app.route("/mine")
def mine():
	responses = api.start_mining()
	dump = []
	for res in responses:
		dump.append(json.dumps(res, indent=4))
	return '\n------------------------------\n'.join(dump)

# if __name__ == "__main__":
#     app.run(host='127.0.0.1', debug=True, port=80)
