from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


class Book(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    book = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

#db.create_all()
class Myform(FlaskForm):
      bookname=StringField("bookname",validators=[DataRequired()])
      author=StringField("author",validators=[DataRequired()])
      rating=SelectField("rating",choices=["1","2","3","4","5"],validators=[DataRequired()])
      submit=SubmitField("submit")

class rateform(FlaskForm):
    newrating=StringField("new rating",validators=[DataRequired()])
@app.route('/')
def home():
    all_books=db.session.query(Book).all()
    return render_template("index.html",list=all_books)


@app.route("/add",methods=['GET','POST'])
def add():
    form=Myform()
    if request.method =="POST":
        new=Book(book=f"{form.bookname.data}",author=f"{form.author.data}",rating=f"{form.rating.data}")
        db.session.add(new)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('add.html',form=form)
@app.route('/delete')
def delete():
    id =request.args.get('id')
    book =Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/rating",methods=['GET','POST'])
def edit():
    form=rateform()
    id=request.args.get('id')
    if request.method=="POST":
       book=Book.query.get(id)
       book.rating=f"{form.newrating.data}"
       db.session.commit()
       return redirect(url_for('home'))

    return render_template('rating.html',form=form)

if __name__ == "__main__":
    app.run(debug=True)

