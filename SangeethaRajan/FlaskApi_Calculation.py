
"""""
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def task():
    return 'flask task'


@app.route('/api/v1/question/add',methods=['POST'])
def calculation():
  if request.method=='POST':
     num1 = request.args.get('num1')
     num2 = request.args.get('num2')
     result = int(num1)+int(num2)
  else:
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
"""""
from flask import Flask,request,jsonify
app = Flask(__name__)

@app.route('/')
def task():
    return 'flask task'

@app.route('/addition', methods=['POST','GET'])
def addition():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    result = int(num1) + int(num2)
    return jsonify({'calculation':add,'The sum is:':result})
if __name__ == '__main__':
    app.run()


