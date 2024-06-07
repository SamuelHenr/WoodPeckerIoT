from order import *
from flask import Flask, request
app = Flask(__name__)
order = Order()

@app.route('/execute', methods=['POST'])
def result():
    return order.execute(request.form['tickets'], request.form['threshold'])