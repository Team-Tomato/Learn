from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, func
from dotenv import load_dotenv
from flask_mail import Mail, Message
import os

app = Flask(__name__)

APP_ROOT = os.path.dirname(__file__)   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

app.config.from_object(os.getenv('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Mail settings
mail_settings = {
  "MAIL_SERVER": 'smtp.gmail.com',
  "MAIL_PORT": 465,
  "MAIL_USE_TLS": False,
  "MAIL_USE_SSL": True,
  "MAIL_USERNAME": os.getenv('EMAIL_USER'),
  "MAIL_PASSWORD": os.getenv('EMAIL_PASSWORD')
}
print(os.getenv('EMAIL_PASSWORD'))
print(os.getenv('EMAIL_USER'))
app.config.update(mail_settings)
mail = Mail(app)

from models import Question

@app.route("/", methods=['GET'])
def get():
  return "<h1>Team Tomato welcome you</h1>"

@app.route("/api/v1/question/add", methods=['POST'])
def add_question():
  question_data = request.get_json()['question']

  subjectName = question_data['subjectName']
  shortForm = question_data['shortForm']
  staff = question_data['staff']
  year = question_data['year']
  url = question_data['url']

  try:
    question=Question(
        subjectName = subjectName,
        shortForm = shortForm,
        staff = staff,
        year = year,
        url = url
     )
    db.session.add(question)
    db.session.commit()
    res = {
      'id': question.id,
      'subjectName': question.subjectName,
      'shortForm': question.shortForm,
      'staff': question.staff,
      'year': question.year,
      'url': question.url
    }
    return jsonify(res)
  except Exception as e:
    return(str(e))

@app.route("/api/v1/question", methods=['GET'])
def get_all_questions():
  try:
    questions = Question.query.all()
    return  jsonify([e.serialize() for e in questions])
  except Exception as e:
    return(str(e))

@app.route("/api/v1/question/<id_>", methods=['GET'])
def get_question_by_id(id_):
  try:
    question = Question.query.filter_by(id=id_).first()
    return jsonify(question.serialize())
  except Exception as e:
    return(str(e))

@app.route("/api/v1/question/search", methods=['GET'])
def search_question():
  try:
    search_str = "%"+request.args.get('search_str')+"%"
    questions = Question.query.filter(or_(Question.subjectName.ilike(search_str), Question.staff.ilike(search_str), Question.shortForm.ilike(search_str)))
    print(questions)
    return  jsonify([e.serialize() for e in questions])
  except Exception as e:
    return(str(e))

@app.route("/api/v1/contactus", methods=['POST'])
def contact_us():
  try:
    contact_data = request.get_json()['contact']
    name = contact_data['name']
    email = contact_data['email']
    message = contact_data['message']
    __send_email(os.getenv('EMAIL_SUB'), [email])
    res = {
        'status': "Submission successful",
        'name': name,
        'email': email,
        'message': message
    }
    return jsonify(res)
  except Exception as e:
    return (str(e)) 

def __send_email(sub, recipient_list):
  msg = Message(subject=sub,
              sender = (os.getenv('MAIL_SENDER_NAME'), app.config.get("MAIL_USERNAME")),
              recipients = recipient_list,
              body = "This is a test email I sent with Gmail and Python!")
  mail.send(msg)

  from models import Book

@app.route("/add")
def add_book():
    name=request.args.get('name')
    author=request.args.get('author')
    subject=request.args.get('subject')
    try:
        book=Book(
            name=name,
            author=author,
            subject=subject
        )
        db.session.add(book)
        db.session.commit()
        return "Book added. book id={}".format(book.id)
    except Exception as e:
	    return(str(e))

@app.route("/getall")
def get_all():
    try:
        books=Book.query.all()
        return  jsonify([e.serialize() for e in books])
    except Exception as e:
	    return(str(e))

@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        book=Book.query.filter_by(id=id_).first()
        return jsonify(book.serialize())
    except Exception as e:
	    return(str(e))


@app.route("/search", methods=['GET'])
def search_book():
  try:
    search_str = "%"+request.args.get('search_str')+"%"
    books = Book.query.filter(or_(Book.name.ilike(search_str), Book.author.ilike(search_str), Book.subject.ilike(search_str)))
    print(books)
    return  jsonify([e.serialize() for e in books])
  except Exception as e:
    return(str(e))


if __name__ == '__main__':
    app.run()
