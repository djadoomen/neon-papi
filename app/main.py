from flask import Flask

import api_fetcher as api

app = Flask(__name__)

@app.route("/")
def index():
    return api.send_request('admin_peers').text

@app.route("/balance")
def balance():
	return api.send_request('eth_getBalance', ["0xb936b619831b77910fb38eed3f80791de6ca21b7", "latest"]).text

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


# if __name__ == "__main__":
#     app.run(host='127.0.0.1', debug=True, port=80)
