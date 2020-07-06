from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
@app.route("/single")
def maild():
    msg = Message('Team Flask', sender="", recipients=['vickykarthy123@gmail.com'])
    msg.body = "Team Flask welcomes You"
    mail.send(msg)
    return "success"


@app.route("/multiple")
def mails():
    user = ["vickykarthy123@gmail.com"]
    for i in user:
        msg = Message('Team Flask', sender='', recipients=[i])
        msg.body = "Team Flask welcomes You"
        mail.send(msg)
    return "success"
if __name__ == '__main__':
    app.run(debug=True)