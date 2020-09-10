from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/sum', methods=['GET', 'POST'])

def get_values():
   value1 = request.args.get('val1')
   value2 = request.args.get('val2')
   return jsonify({'data':f'<p>The result is: {int(value1)+int(value2)}</p>'})


if __name__ == '__main__':
    app.run()