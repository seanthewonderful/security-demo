from tokenize import String
from turtle import width
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-collection.db'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_API_KEY = "bd67cba2f6db962030938111227e24da"
MOVIE_DB_API_DETAILS = "https://api.themoviedb.org/3/movie"

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), unique=True, nullable=False)
    rating = db.Column(db.Float(50), nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)
    
# db.create_all()


# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )

# db.session.add(new_movie)
# db.session.commit()

class EditForm(FlaskForm):
    rating = FloatField('Your rating out of 10:', validators=[DataRequired()])
    review = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class AddForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add this title')
    

@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating.desc()).all()
    for i in range(len(movies)):
        movies[i].ranking = i + 1
    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route("/edit/<movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    form = EditForm()
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        new_rating = form.rating.data
        new_review = form.review.data
        movie.rating = new_rating
        movie.review = new_review
        db.session.commit()
        
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=form)


@app.route('/delete/<movie_id>')
def delete(movie_id):
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        title = form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": title})
        data = response.json()['results']
        return render_template('select.html', data=data)
    return render_template('add.html', form=form)


@app.route('/select/<movie_id>', methods=["GET", "POST"])
def select(movie_id):
    data = requests.get(f"{MOVIE_DB_API_DETAILS}/{movie_id}?api_key={MOVIE_DB_API_KEY}").json()
    # print(data)
    new_movie = Movie(
        title=data['title'],
        year=data['release_date'].split("-")[0],
        description=data['overview'],
        img_url="https://image.tmdb.org/t/p/original"+data['backdrop_path']
        )
    db.session.add(new_movie)
    db.session.commit()
    new_id = new_movie.id
    return redirect(url_for('edit', movie_id=new_id))


if __name__ == '__main__':
    app.run(debug=True)
