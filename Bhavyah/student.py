from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
 
app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Ramesh@17@localhost/Student"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Studentdata(db.Model):
    __tablename__ = 'StudentTable'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    course = db.Column(db.String())
    year = db.Column(db.Integer())

    def __init__(self,id, name, course, year):
        self.id=id
        self.name = name
        self.course = course
        self.year = year
@app.route('/StudentTable', methods=['POST', 'GET'])
def insert_data():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_student = Studentdata(id=data['id'], name=data['name'], course=data['course'], year=data['year'])
            db.session.add(new_student)
            db.session.commit()
            return "Student has been created successfully."
        else:
            return "The request payload is not in JSON format"

    elif request.method == 'GET':
        Students = Studentdata.query.all()
        results = [
            {
                "id":student.id,
                "name": student.name,
                "course": student.course,
                "year": student.year
            } for student in Students]

        return {"count": len(results), "Students": results}
@app.route('/StudentTable/<student_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_student(student_id):
    student = Studentdata.query.get_or_404(student_id)

    if request.method == 'GET':
        response = {
            "id": student.id,
            "name": student.name,
            "course": student.course,
            "year": student.year
        }
        return {"message": "success", "student": response}

    elif request.method == 'PUT':
        data = request.get_json()
        student.id=data['id']
        student.name = data['name']
        student.course = data['course']
        student.year = data['year']
        db.session.add(student)
        db.session.commit()
        return "successfully updated"

    elif request.method == 'DELETE':
        db.session.delete(student)
        db.session.commit()
        return  "successfully deleted."
    if __name__=='__main__':
        app.run(debug=True)
        
    
    
