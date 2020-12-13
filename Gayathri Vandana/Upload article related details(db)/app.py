import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import validators
app2 = Flask(__name__)
app2.config.from_object(os.getenv('APP_SETTINGS'))
app2.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app2.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user1:test123@localhost/details"
app2.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app2)

class Details(db.Model):
    __tablename__ = 'details'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    author = db.Column(db.String())
    category = db.Column(db.String())
    link = db.Column(db.String())

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'category':self.category,
            'link' :self.link}

@app2.route('/api/v1/article/new', methods=['POST'])
def add_details():
    details_data = request.get_json()['details']

    name = details_data['name']
    author = details_data['author']
    category = details_data['category']
    link = details_data['link']
    valid = validators.url(link)
    if ((valid == True) and (len(author)>2 or len(author)<20)):
        try:
            details = Details(
                name=name,
                author=author,
                category=category,
                link=link)
            db.session.add(details)
            db.session.commit()
            res = {
                'name': details.name,
                'author': details.author,
                'category': details.category,
                'link': details.link,
            }
        except Exception as e:
            return (str(e))
        return jsonify(res)
    else:
        return jsonify('Enter the input in proper form')
@app2.route('/api/v1/details', methods=['GET'])
def get_details():
  try:
    details = Details.query.all()
    return  jsonify([e.serialize() for e in details])
  except Exception as e:
    return(str(e))
if __name__ == '__main__':
#    db.create_all()
    app2.run()