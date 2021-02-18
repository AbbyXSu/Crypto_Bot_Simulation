import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_coinValue():
    Value_c = random.randint(0, 3000)
    return { 'Coin Value': Value_c }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')