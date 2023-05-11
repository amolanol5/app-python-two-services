from flask import Flask
from data import colors
import os
import json

port_value = os.environ.get('APP_SERVICE_DATA_PORT')

app = Flask(__name__)
@app.route("/")
def root():
    return "service data"

@app.route("/data")
def data():
    return json.dumps(colors)


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=port_value)