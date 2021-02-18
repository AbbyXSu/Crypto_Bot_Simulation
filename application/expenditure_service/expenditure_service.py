import random
from flask import Flask,  jsonify

app = Flask(__name__)

@app.route('/expense', methods=['GET'])
def get_expenditrue():
    Expense = random.randint(-5000, 0)
    return jsonify ({ 'Expense': Expense })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5002')