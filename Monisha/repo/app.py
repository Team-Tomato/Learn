import os
from flask import Flask, jsonify
from github import Github
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)


app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Repository


@app.route("/")
def home():
    g = Github("7330eb02f7b1b9201b850262ff6e2b84c48685d2")
    user = g.get_user()
    repo = g.get_user().get_repos()
    l = []
    for r in repo:
      l.append(r.name)
    try:
        details = Repository(
        username = user.login,
        repos = l
        )
        db.session.add(details)
        db.session.commit()
        det=Repository.query.all()
        return jsonify([e.serialize() for e in det])
        # return "Repos added. Repo id : {}, User : {} ".format(details.id, user.login)
    except Exception as e:
	    return(str(e))
     

if __name__ == "__main__":
    app.run(debug=True)

