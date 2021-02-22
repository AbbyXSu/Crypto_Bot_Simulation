from sqlalchemy import desc
import requests
from flask import json, jsonify
from flask import Response
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy.ext.declarative import DeclarativeMeta

app = Flask(__name__)
app.config['SECRET_KEY'] = '88dd6a6854b7f1901b7f01d353186c6a'
app.config['SQLALCHEMY_DATABASE_URI'] =os.environ.get('DATABASE_URI')
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

db.create_all()




# class AlchemyEncoder(json.JSONEncoder):

#     def default(self, obj):
#         if isinstance(obj.__class__, DeclarativeMeta):
#             # an SQLAlchemy class
#             fields = {}
#             for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
#                 data = obj.__getattribute__(field)
#                 try:
#                     json.dumps(data) # this will fail on non-encodable values, like other classes
#                     fields[field] = data
#                 except TypeError:
#                     fields[field] = None
#             # a json-encodable dict
#             return fields
#         print('***********')
#         return json.JSONEncoder.default(self, obj)


def row_dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d


@app.route('/report_engine',methods=["GET","POST"])
def get_reports():  
    revenue = requests.get("http://revenue_service:5001/revenue").json().get('Revenue','0')
    print(revenue)
    expense = requests.get("http://expenditure_service:5002/expense").json().get('Expense','0')
    result_raw = requests.post("http://report_aggregate_service:5003/report_generator", json={'revenue':revenue, 'expense':expense})
    if result_raw.status_code == 200 or result_raw.status_code == 201:
        result = result_raw.json()
    else:
        result = {}

    PLtype = result.get('PLtype', '')
    income = result.get('income', '')
    efficiency_ratio = result.get('efficiency_ratio', '')

    report = Reports(revenue=revenue,expense =expense, income=income, efficiency_ratio=efficiency_ratio, PLtype=PLtype)
    
    db.session.add(report)
    db.session.commit()
    reports = db.session.query(Reports).order_by(Reports.id.desc()).all()
    latestItem= db.session.query(Reports).order_by(Reports.id.desc()).first()
    print(reports)
    reports = [row_dict(rep) for rep in reports]
    latestItem = row_dict(latestItem)

    return jsonify({'reports':reports,'latest_item':latestItem})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5004')