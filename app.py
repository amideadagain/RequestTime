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
    start_time = time.monotonic()
    result = []
#    for i in range(1000000):
#        i += 1
    for i in range(quantity):
        result.append({})
        result[i]['uuid'] = str(uuid4())
        result[i]['date'] = time.asctime(time.localtime())
    return render_template('requests.html', result=result, request_time=f"{int((time.monotonic() - start_time)*1000)}ms")


hello_user()
