import random
from flask import Flask, request,  jsonify

app = Flask(__name__)

@app.route('/report_generator', methods=['POST'])
def get_performance():

    revenue = int(request.args.get('revenue'))
    expense = int(request.args.get('expense'))


    if not revenue:
        renenue = 500

    if not expense:
        expense = -500

    type = "Break Even"

    income = revenue - expense

    is_loss = income < 0
    is_profits = income > 0
    is_breakeven = income = 0

    if is_loss:
        print('loss detected')
        type = "Loss"

    if is_profits:
        print('profit detected')
        type = "profit"
    
    if is_breakeven:
        print('Break-even')
        type = "Break-even"

    efficiency_ratio = round(revenue (expense / revenue) * 100)

    return  jsonify ({
        'income': income,
        'Efficiency_ratio': efficiency_ratio,
        'type': type
    })



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5003')