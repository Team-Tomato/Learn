from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

app2=Flask(__name__)
app2.config['SQLALCHEMY_DATABASE_URI']="postgresql://user1:test123@localhost/employee"
app2.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app2)
#migrate=Migrate(app2,db)
class Employee(db.Model):
    __tablename__='company2'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String())
    age=db.Column(db.String())
    address=db.Column(db.String())
    salary=db.Column(db.String())
    def __init__(self,name,age,address,salary):
        self.name=name
        self.age=age
        self.address=address
        self.salary=salary
    def __repr__(self):
        return f"<Emp {self.name}>"

@app2.route('/company2',methods=['POST','GET'])
def handle_company2():
    if request.method=='POST':
        if request.is_json:
            data=request.get_json()
            new_company=Employee(name=data['name'],age=data['age'],address=data['address'],salary=data['salary'])
            db.session.add(new_company)
            db.session.commit()
            return "successfully created"
        else:
            return {"error:" "The request payload is not in JSON format"}
    elif request.method=='GET':
        company2=Employee.query.all()
        results=[
            {
                "name":company.name,
                "age":company.age,
                "address":company.address,
                "salary":company.salary
            }for company in company2]
        return {"count": len(results), "company2":results}
db.create_all()
#app2.run()

@app2.route('/company2/<company_id>',methods=['GET','PUT','DELETE'])
def handles_company2(company_id):
    company=Employee.query.get_or_404(company_id)
    if request.method=='GET':
        response={
            "name":company.name,
            "age":company.age,
            "address":company.address,
            "salary":company.salary
        }
        return {"message":"sucess","company":response}
    elif request.method=='PUT':
        data=request.get_json()
        company.name=data['name']
        company.age=data['age']
        company.address=data['address']
        company.salary=data['salary']
        db.session.add(company)
        db.session.commit()
        return "successfully updated"
    elif request.method=='DELETE':
        db.session.delete(company)
        db.session.commit()
        return "successfully deleted"
app2.run()