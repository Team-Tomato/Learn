from flask import Flask
from flask import jsonify

app1 = Flask(__name__)


@app1.route('/<int:num1>/<int:num2>/<method>')
def add(num1, num2, method):
    if method == 'Add':
        return jsonify({'Response code': 200, 'Addition': num1+num2})
    else:
        return jsonify({'Response code': 400, 'Error': 'Invalid input'})


@app1.route('/<int:num1>/<int:num2>/<method>')
def sub(num1, num2, method):
    if method == 'Sub':
        return jsonify({'Response code': 200, 'Subtraction': num1-num2})
    else:
        return jsonify({'Response code': 400, 'Error': 'Invalid input'})


@app1.route('/<int:num1>/<int:num2>/<method>')
def mul(num1, num2, method):
    if method == 'Mul':
        return jsonify({'Response code': 200, 'Multiplication': num1*num2})
    else:
        return jsonify({'Response code': 400, 'Error': 'Invalid input'})


@app1.route('/<int:num1>/<int:num2>/<method>')
def div(num1, num2, method):
    if num2 != 0 and method == 'Div':
        return jsonify({'Response code': 200, 'Division ': num1/num2})
    else:
        return jsonify({'Response code': 400, 'Error': 'Invalid input'})


if __name__ == '__main__':
    app1.run(debug=True)



