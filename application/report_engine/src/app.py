from sqlalchemy import desc
import requests
from flask import jsonify
from flask import Response
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = '88dd6a6854b7f1901b7f01d353186c6a'
app.config["SQLALCHEMY_DATABASE_URI"] =os.getenv('DATABASE_URI')
    # environment: 
    #   - DATABASE_URI=mysql+pymysql://root:${DB_PASSWORD}@mysql/MySQLDB
    #   - MYSQL_ROOT_PASSWORD=${DB_PASSWORD} 
print('db uri: ', os.getenv('DATABASE_URI'))
db = SQLAlchemy(app)

class Reports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    revenue = db.Column(db.String(500), nullable=False)
    expense = db.Column(db.String(500), nullable=False)
    PLtype = db.Column(db.String(500), nullable=False)
    income = db.Column(db.String(500), nullable=False)
    efficiency_ratio = db.Column(db.String(500), nullable=False)


@app.route('/report_engine',methods=["GET","POST"])
def get_reports():  
    revenue = requests.get("http://revenue_service:5001/revenue")
    expense = requests.get("http://expenditure_service:5002/expense")
    result = requests.post("http://report_aggregate_service:5003/report_generator", json={'revenue':revenue.text, 'expense':expense.text})

    PLtype = result['PLtype']
    income = result['income']
    efficiency_ratio = result['efficiency_ratio']

    report = Reports(revenue=revenue.text, income=income.text, efficiency_ratio=efficiency_ratio.text, PLtype=PLtype.text)
    
    db.session.add(report)
    db.session.commit()
    reports = Reports.query.order_by(Reports.id.desc()).limit(5)
    latestItem= Reports.query.order_by(Reports.id).first()

    return jsonify(str(reports),str(latestItem),mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5004')