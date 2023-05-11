from flask import Flask
import requests
import os
import json

service_data = os.environ.get('APP_SERVICE_DATA')
port_value = os.environ.get('APP_SERVICE_CONSUMER_DATA_PORT')


app = Flask(__name__)
@app.route("/")
def root():
    return "service consuming data"

@app.route("/procesing_data")
def procesing_data():
#   response = requests.get("https"service_data + ":7070/data")
    response = requests.get("http://" + service_data + ":7070/data")
    data = json.loads(response.text)
    
    return "El color6 es: " + data.get('color6')
  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port_value)