from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:viswa@475@localhost/student'
db = SQLAlchemy(app)

class Movies(db.Model):
    __tablename__ = 'mv'
    name = db.Column(db.String(255), primary_key=True)
    casts = db.Column(db.String(80), unique=True, nullable=False)
    genres = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name, casts, genres):
        self.name = name
        self.casts = casts
        self.genres = genres

db.create_all()
movies = [
    {
        "name": "The Shawshank Redemption",
        "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"]
    },
    {
       "name": "The Godfather ",
       "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
       "genres": ["Crime", "Drama"]
    }
]
@app.route('/')


@app.route('/movies', methods=['POST'])
def add_movie():
    if request.method == 'POST':
        name = request.form['name']
        casts = request.form['casts']
        genres = request.form['genres']

        my_data = Movies(name, casts, genres)
        db.session.add(my_data)
        db.session.commit()

        flash("Employee Inserted Successfully")

        return redirect(url_for('Index'))

@app.route('/movies', methods = ['GET', 'POST'])
def update_movie():
        if request.method == 'POST':
            my_data = Movies.query.get(request.form.get('id'))

            my_data.name = request.form['name']
            my_data.casts = request.form['casts']
            my_data.genres = request.form['genres']

            db.session.commit()
            flash("Employee Updated Successfully")

            return redirect(url_for('Index'))

@app.route('/movies/<int:index>', methods=['DELETE'])
def delete_movie(index):
    my_data = Movies.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")

    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run()