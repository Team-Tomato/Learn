from app import db

class Repository(db.Model):
    __tablename__ = 'user_repos'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    repos = db.Column(db.String())

    def __init__(self, username, repos):
            self.username = username
            self.repos = repos
    
    def __repr__(self):
        return '<id{}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id, 
            'username': self.username,
            'repos': self.repos
        }
