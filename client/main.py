from flask import Flask, render_template, url_for
app = Flask(__name__)

order = Order()

@app.route('/hello/')
def hello(name=None):
    return render_template('hello.html', path=url_for('static', filename='sendRequest.js'))
