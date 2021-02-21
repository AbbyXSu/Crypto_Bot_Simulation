from application import app, db
from .models import Reports
from sqlalchemy import desc
import requests
from flask import jsonify
from flask import Response

@app.route('/report_engine',methods=["GET","POST"])
def get_reports():  
    revenue = requests.get("http://revenue_service:5001/revenue")
    expense = requests.get("http://expenditure_service:5002/expense")
    PLtype,income, efficiency_ratio = requests.post("http://report_aggregate_service:5003/report_generator", json={'revenue':revenue.text, 'expense':expense.text})
    
    report = Reports(revenue=revenue.text, income=income.text, efficiency_ratio=efficiency_ratio.text, PLtype=type.text)
    
    db.session.add(report)
    db.session.commit()
    reports = Reports.query.order_by(Reports.id.desc()).limit(5)
    latestItem= Reports.query.order_by(Reports.id).first()

    return jsonify(str(reports),str(latestItem),mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5004')