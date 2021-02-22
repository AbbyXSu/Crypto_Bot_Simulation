import random
from flask import Flask, request,  jsonify,abort
from requests.models import Response

app = Flask(__name__)

@app.route('/report_generator', methods=['POST'])
def get_performance():
    if not request.json:
        abort(400,"Request nor found")
    revenue = int(request.json.get('revenue',  '0'))
    expense = int(request.json.get('expense', '0'))

    print (request.json)

    if not revenue:
        revenue = 500

    if not expense:
        expense = -500

    PLtype = "Break Even"

    income = revenue + expense

    is_loss = income < 0
    is_profits = income > 0
    is_breakeven = income = 0

    if is_loss:
        print('loss detected')
        PLtype = "Loss"

    if is_profits:
        print('profit detected')
        PLtype = "profit"
    
    if is_breakeven:
        print('Break-even')
        PLtype = "Break-even"

    print (expense)
    print(revenue)
    print(income)

    
    if expense != 0:
        efficiency_ratio = round((income/expense) * 100)
    else:
        efficiency_ratio =100

    return  jsonify ({
        'income': income,
        'Efficiency_ratio': efficiency_ratio,
        'PLtype': PLtype
    })



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5003')