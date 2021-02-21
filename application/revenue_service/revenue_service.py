
import random
from flask import Flask,  jsonify

app = Flask(__name__)

@app.route('/revenue', methods=['GET'])
def get_revenue():
    Revenue = random.randint(0, 10000)
    return  jsonify ({ 'Revenue': Revenue })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')