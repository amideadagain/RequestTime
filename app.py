from flask import Flask, render_template
from uuid import uuid4
import time

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_user():
    return "<p>Hello</p>"


@app.route('/get_data/', defaults={'quantity': 1})
@app.route('/get_data/<int:quantity>')
def number(quantity):
    result = []
    for i in range(quantity):
        result.append({})
        result[i]['uuid'] = str(uuid4())
        result[i]['time'] = 'TIME'
        result[i]['date'] = time.asctime(time.localtime())
    return render_template('requests.html', result=result)


hello_user()
