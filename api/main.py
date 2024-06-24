from order import *
from flask import Flask, request
app = Flask(__name__)
order = Order()

@app.route('/execute', methods=['POST'])
def result():
    result = order.execute(int(request.form['tickets']), int(request.form['threshold']), int(request.form['timestamp']))
    return result