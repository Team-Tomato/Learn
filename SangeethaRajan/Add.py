from flask import Flask,request,jsonify
app = Flask(__name__)

@app.route('/')
def task():
    return 'Flask Task'

@app.route('/calculate/add', methods=['POST','GET'])
def add():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    result= int(num1) + int(num2)
    return jsonify({'Calculation':'Addtion', 'The sum of 2 nos:': result})

if __name__ == '__main__':
    app.run()
