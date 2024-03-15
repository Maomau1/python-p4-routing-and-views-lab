#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print (parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    return (f'{n}\n' for n in range(parameter))

@app.route('/math/<int:param1>/<string:operation>/<int:param2>')
def math(param1,operation,param2):
    if operation == 'div':
        result = param1 / param2
    elif operation == '+':
        result = param1 + param2
    elif operation == '-':
        result = param1 - param2
    elif operation == '*':
        result = param1 * param2
    elif operation == '%':
        result = param1 % param2
    return f'{result}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
