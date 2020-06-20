import os
from flask import Flask, jsonify
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from flask_sqlalchemy import SQLAlchemy
import psycopg2

con = psycopg2.connect(database="postgres", user="moni", password="Kitty2802", host="127.0.0.1", port="5432")
cur = con.cursor()

def details():
    try:
        request_repo = requests.get('https://api.github.com/orgs/Team-Tomato/repos')
        repo = request_repo.json()
        con_list = []

        for p in range(1,3):
            for j in range(0,len(repo)): 
                no = str(p)
                url =  'https://api.github.com/repos/Team-Tomato/'+repo[j]['name']+'/contributors?page='+no
                print(url)
                request = requests.get(url)
                json = request.json()

                for i in range(0,len(json)):
                    t = ()
                    t = t + (json[i]['login'],json[i]['avatar_url'],json[i]['html_url'],)
                    con_list += (t,)
        
        c = list(set(con_list))
        list_str = str(c)
        list_str = list_str[1:-1]

        cur.execute("INSERT INTO contributors VALUES " + list_str + "ON CONFLICT (username) DO NOTHING")
        print("Updated")
        con.commit()

    except Exception as e:
	    return(str(e))

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Contributors

sched = BackgroundScheduler(daemon=True)
sched.add_job(details,'interval',minutes=15)
sched.start()  

@app.route("/team-tomato/contributors")
def show():
  d = Contributors.query.all()
  return jsonify([e.serialize() for e in d])
    
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

