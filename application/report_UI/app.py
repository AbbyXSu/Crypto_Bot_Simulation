from flask import Flask
import requests
from flask import render_template

app = Flask(__name__)

@app.route('/',methods=["GET"])
def index():  
    result_raw = requests.get("http://report_engine:5004/report_engine")
    if result_raw.status_code == 200 or result_raw.status_code == 201:
        result = result_raw.json()
    else:
        result = {}

    reports = result.get('reports', '')
    latestItem = result.get('latest_item', '')

    return render_template("index.html",reports = reports, latestItem = latestItem)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')