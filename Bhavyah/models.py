from app import db


class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    subjectName = db.Column(db.String())
    shortForm = db.Column(db.String())
    staff = db.Column(db.String())
    year = db.Column(db.Integer)
    url = db.Column(db.String())

    def __init__(self, subjectName, shortForm, staff, year, url):
        self.subjectName = subjectName
        self.shortForm = shortForm
        self.staff = staff
        self.year = year
        self.url = url

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'subjectName': self.subjectName,
            'shortForm': self.shortForm,
            'staff':self.staff,
            'year' :self.year,
            'url' :self.url
        }
class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    author = db.Column(db.String())
    subject = db.Column(db.String())

    def __init__(self, name, author, subject):
        self.name = name
        self.author = author
        self.subject = subject

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'author': self.author,
            'subject':self.subject
        }
