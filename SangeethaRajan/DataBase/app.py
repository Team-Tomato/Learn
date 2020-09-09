from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Sangee01@localhost:5432/Simple_DB'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(200),nullable=False)
    Phone_no = db.Column(db.String(10), nullable=False)
    Email = db.Column(db.String(200), nullable=False)
    City = db.Column(db.String(200), nullable=False)
    State = db.Column(db.String(200), nullable=False)
    Pincode = db.Column(db.String(200), nullable=False)


    def __repr__(self):
        return '<Detail %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['Username']
        phone = request.form['Phone_no']
        email= request.form['Email']
        city= request.form['City']
        state= request.form['State']
        pincode= request.form['Pincode']
        new_contact = User(Username=name,Phone_no=phone
        ,Email=email,City=city,State=state,Pincode=pincode)

        try:
            db.session.add(new_contact)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        contacts = User.query.order_by(User.Username).all()
        return render_template('index.html', contacts=contacts)


if __name__ == "__main__":
    app.run(debug=True)