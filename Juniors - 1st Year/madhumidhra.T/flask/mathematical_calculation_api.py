from flask import *
app = Flask(__name__)

@app.route('/add/<a>/<b>/')
def add(a,b):
    C = int(a) + int(b)
    return("Addition Of Two Numbers"+" "+ a +" "+"and"+" "+ b +" "+"is"+" "+str(C))


@app.route('/sub/<a>/<b>')
def sub(a,b):
    C = int(a) - int(b)
    return ("Subraction Of Two Numbers" + " " + a + " " + "and" + " " + b + " " + "is" + " " + str(C))


@app.route('/mul/<a>/<b>')
def mul(a,b):
    C = int(a) * int(b)
    return ("Multiplication Of Two Numbers" + " " + a + " " + "and" + " " + b + " " + "is" + " " + str(C))

@app.route('/div/<a>/<b>')
def div(a,b):
    try:
        C = int(a) / int(b)
        return ("Division Of Two Numbers" + " " + a + " " + "and" + " " + b + " " + "is" + " " + str(C))
    except:
        return ("Error Division By Zero Is Not Possible")

@app.route('/exact_div/<a>/<b>')
def exact_div(a,b):
    try:
        C = int(a) // int(b)
        return ("Division Of Two Numbers" + " " + a + " " + "and" + " " + b + " " + "is" + " " + str(C))
    except:
        return ("Error Division By Zero Is Not Possible")

@app.route("/user/operation")
def user(operation):
    if operation == 'add':
        return redirect(url_for('add'))
    if operation == 'sub':
        return redirect(url_for('sub'))
    if operation == 'mul':
        return redirect(url_for('mul'))
    if operation == 'div':
        return redirect(url_for('div'))
    if operation == 'exact_div':
        return redirect(url_for('exact_div'))

if __name__ == '__main__':
    app.run(debug=True)