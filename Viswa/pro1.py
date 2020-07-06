from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Viswa@475@localhost/student'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    author = db.Column(db.String(255))
    genre = db.Column(db.String(255))
    
    def __init__(self, name, author,genre):
        self.name = name
        self.author = author
        self.genre = genre
    

@app.route('/')
@app.route('/data', methods=['POST', 'GET'])
def data():
    
    
    if request.method == 'POST':
        body = request.json
        name = body['name']
        author = body['author']
        genre = body['genre']

        data = User(name, author,genre)
        db.session.add(data)
        db.session.commit()

        return jsonify({
            'status': 'Data is added to PostgreSQL!',
            'name': name,
            'author': author,
            'genre': genre
        })
    
  
    if request.method == 'GET':
        data = User.query.order_by(User.id).all()
        dataJson = []
        for i in data:
            dataDict = {
                'id': i.id,
                'name': i.name,
                'author': i.author,
                'genre': i.genre
            }
            dataJson.append(dataDict)
        return jsonify(dataJson)

@app.route('/data/<id>', methods=['GET', 'DELETE', 'PUT'])
def onedata(id):

    # GET a specific data by id
    if request.method == 'GET':
        data = User.query.get(id)
        dataDict = {
            'id': data.id,
            'name': data.name,
            'author': data.author,
            'genre': data.genre
        }
        return jsonify(dataDict)
        
    # DELETE a data
    if request.method == 'DELETE':
        delData = User.query.filter_by(id=id).first()
        db.session.delete(delData)
        db.session.commit()
        return jsonify({'status': 'Data '+id+' is deleted from PostgreSQL!'})

    # UPDATE a data by id
    if request.method == 'PUT':
        body = request.json
        newName = body['name']
        newAuthor = body['author']
        newGenre = body['genre']
        editData = User.query.filter_by(id=id).first()
        editData.name = newName
        editData.author = newAuthor
        editData.genre = newGenre
        db.session.commit()
        return jsonify({'status': 'Data '+id+' is updated from PostgreSQL!'})

if __name__ == '__main__':
    app.debug = True
    db.create_all()
    app.run()