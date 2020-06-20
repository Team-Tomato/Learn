from app import db

class Contributors(db.Model):
    __tablename__ = 'contributors'

    username = db.Column(db.String(), unique=True,  primary_key=True)
    avatar = db.Column(db.String())
    htmlurl = db.Column(db.String())


    def __init__(self, username, avatarimg, htmlurl):
            self.username = username
            self.avatar = avatar
            self.htmlurl = htmlurl

    
    def __repr__(self):
        return '<name={}>'.format(self.username)

    def serialize(self):
        return {
            'username': self.username,
            'avatar': self.avatar,
            'htmlurl': self.htmlurl
        }
