from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def task():
    return 'flask task'


@app.route('/api/v1/question/add')
def calculation():
  try:
     num1 = request.args.get('num1')
     num2 = request.args.get('num2')
     result = int(num1)+int(num2)
     return jsonify({'Response code': 200, 'Addition': result})
  except:
      return jsonify({'Response code': 400, 'Error': 'Invalid input'})


@app.route('/api/v1/question/sub')
def calculation():
  try:
     num1 = request.args.get('num1')
     num2 = request.args.get('num2')
     result = int(num1)-int(num2)
     return jsonify({'Response code': 200, 'Subtraction': result})
  except:
      return jsonify({'Response code': 400, 'Error': 'Invalid input'})


@app.route('/api/v1/question/mul')
def calculation():
  try:
     num1 = request.args.get('num1')
     num2 = request.args.get('num2')
     result = int(num1)*int(num2)
     return jsonify({'Response code': 200, 'Multiply': result})
  except:
      return jsonify({'Response code': 400, 'Error': 'Invalid input'})


@app.route('/api/v1/question/div')
def calculation():
  try:
     num1 = request.args.get('num1')
     num2 = request.args.get('num2')
     result = int(num1)/int(num2)
     return jsonify({'Response code': 200, 'Division': result})
  except:
      return jsonify({'Response code':  400, 'Error': 'Invalid input'})


if __name__ == '__main__':
    app.run(debug=True)



