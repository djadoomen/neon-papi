from flask import Flask

from api_fetcher import send_request

app = Flask(__name__)

@app.route("/")
def hello():
    return send_request('admin_peers')


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=80)
