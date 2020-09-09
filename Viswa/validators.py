from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_validator import ValidateInteger, ValidateString, ValidateEmail
from sqlalchemy.orm import validates

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.sql import func
from sqlalchemy.orm import joinedload

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Viswa@475@localhost/student'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    author = db.Column(db.String(10))
    genre = db.Column(db.String(8))
    
    def __init__(self, name, author,genre):
        self.name = name
        self.author = author
        self.genre = genre

   
    
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise AssertionError('No Book name provided')

        if len(name) < 3 or len(name) > 13:
            raise AssertionError('Book name must be between 3 and 12 characters')

        return name

    @validates('author')
    def validate_author(self, key, author):
        if not author:
            raise AssertionError('No Author name provided')

        if len(author) < 3 or len(author) > 13:
            raise AssertionError('Author name must be between 3 and 12 characters')

        return author

    @validates('genre')
    def validate_genre(self, key, genre):
        if not genre:
            raise AssertionError('No Genre name provided')

        if len(genre) < 3 or len(genre) > 8:
            raise AssertionError('Genre name must be between 3 and 8 characters')

        return genre


  

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
            'status': 'Data is added to DB',
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
        return jsonify({'status': 'Data '+id+' is deleted from DB'})

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
        return jsonify({'status': 'Data '+id+' is updated from DB'})

if __name__ == '__main__':
    app.debug = True
    db.create_all()
    app.run()