from Flask import app
import requests
from flask import render_template

@app.route('/',methods=["GET"])
def index():  
    reports, latestItem = requests.get("http://localhost:5004/reports")

    return render_template("index.html",reports = reports.text, latestItem = latestItem.text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')