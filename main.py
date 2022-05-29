from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import time
from flask import session




app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)

class Apiform(FlaskForm):
    moviename=StringField("movie name",validators=[DataRequired()])
    submit=SubmitField("search")


class Editform(FlaskForm):
     id=StringField("id...if you are adding new film")
     rating = StringField("rating", validators=[DataRequired()])
     review = StringField("review",validators=[DataRequired()])
     submit = SubmitField("update")
class Myform(FlaskForm):
      id=StringField("id",validators=[DataRequired()])
      title=StringField("title",validators=[DataRequired()])
      year=StringField("year",validators=[DataRequired()])
      description = StringField("description", validators=[DataRequired()])
      rating= StringField("rating", validators=[DataRequired()])
      ranking= StringField("ranking", validators=[DataRequired()])
      review = StringField("review", validators=[DataRequired()])
      img_url = StringField("img url", validators=[DataRequired()])
      submit=SubmitField("submit")


class Movie(db.Model):
    id=db.Column(db.Integer, nullable=False,primary_key=True)
    title=db.Column(db.String(80), unique=True, nullable=False)
    year=db.Column(db.String(80), nullable=False)
    description=db.Column(db.String(220), nullable=False)
    rating=db.Column(db.Float, nullable=False)
    ranking=db.Column(db.Integer,nullable=False)
    review=db.Column(db.String(220), nullable=False)
    img_url=db.Column(db.String(220), nullable=False)


    def __repr__(self):
        return '<User %r>' % self.username
db.create_all()
@app.route('/')
def home():
    all= Movie.query.order_by(Movie.rating).all()

    for i in range( len(all)):

        all[i].ranking = len(all) - i
    db.session.commit()
    return render_template("index.html",all=all)

@app.route('/api',methods=['GET','POST'])
def api():
    form=Apiform()
    if request.method=='POST':
        moviename=form.moviename.data

        pramas = {
            "api_key": "73072590b9f81cc596dc82abc811f99c",
            "query": f"{moviename}",
            "language": "en-US",

            "page": 1
        }
        moviemain = []

        response = requests.get(url="https://api.themoviedb.org/3/search/movie", params=pramas)
        print(response.json()["results"][0])
        for i in range(0, 10):
            m = response.json()["results"][i]["title"]
            des = response.json()["results"][i]["overview"]
            rate = response.json()["results"][i]["vote_average"]
            img_url = response.json()["results"][i]["poster_path"]
            nyear = response.json()["results"][i]["release_date"]
            year = nyear.split("-")[0]
            new = {
                "title": m,
                "year": year,
                "description": des,
                "rating": rate,
                "img_url": f"http://image.tmdb.org/t/p/w500{img_url}"
            }
            moviemain.append(new)
        time.sleep(1)
        session['movies']=moviemain
        print(moviemain)
        return redirect(url_for('select'))
    return render_template('api.html',form=form)

@app.route('/select')
def select():
    movies=session["movies"]
    return render_template('select.html',movies=movies)

@app.route('/add',methods=['GET','POST'])
def add():
    form=Myform()
    if request.method == 'POST':
             new = Movie(
             id=form.id.data,
             title=form.title.data,
             year=form.year.data,
             description=form.description.data,
             rating=form.rating.data,
             ranking=form.ranking.data,
             review=form.review.data,
             img_url=form.img_url.data
             )

             db.session.add(new)
             db.session.commit()
             return redirect(url_for('home'))


    return render_template("add.html",form=form)

@app.route('/edit',methods=['GET','POST'])
def edit():
    form=Editform()
    id = request.args.get('id')
    n = request.args.get('c')

    if request.method == 'POST':
        try:
            movie = Movie.query.get(id)
            movie.rating=form.rating.data
            movie.review=form.review.data
            db.session.commit()
        except:

            movies=session['movies']
            movie=movies[int(n)]
            new = Movie(
                id=form.id.data,
                title=movie["title"],
                year=movie["year"],
                description=movie["description"],
                ranking=form.rating.data,
                rating=form.rating.data,
                review=form.review.data,
                img_url=movie["img_url"]
            )

            db.session.add(new)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html',form=form)

@app.route('/delete')
def delete():
    id = request.args.get('id')
    movie=Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
