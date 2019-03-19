from flask import Flask
from api_fetcher import SendRequest

from controller.request_node import RequestNode

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Flask"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
