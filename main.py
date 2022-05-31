import random
from flask import Flask, render_template, redirect, url_for, session, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)

@app.route('/newpost',methods=["GET","POST"])
def newpost():
    x=datetime.datetime.now()
    year=x.year
    month=x.strftime("%B")
    day=x.strftime("%d")
    date=f"{month}{day},{year}"
    form=CreatePostForm()

    if request.method =="POST":
       new=BlogPost(

           title=form.title.data,
           subtitle=form.subtitle.data,
           author=form.author.data,
           img_url=form.img_url.data,
           body=form.body.data,
           date=date
       )

       db.session.add(new)
       db.session.commit()
       return redirect(url_for('get_all_posts'))
    return render_template('make-post.html',form=form)

@app.route('/delete/<post_id>')
def delete(post_id):
    post=BlogPost.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route('/edit',methods=["GET","POST"])
def edit_post():
     post_id=request.args.get('post_id')
     post=BlogPost.query.get(post_id)
     form=CreatePostForm(

         title=post.title,
         subtitle=post.subtitle,
         author=post.author,
         img_url=post.img_url,
         body=post.body,

     )
     if request.method=="POST":


             post.title=form.title.data
             post.subtitle=form.subtitle.data
             post.author=form.author.data
             post.img_url=form.img_url.data
             post.body=form.body.data

             db.session.commit()
             return redirect(url_for('show_post',index=post_id))
     return render_template('make-post.html',form=form,edit=True)

@app.route("/post/<int:index>")
def show_post(index):
    posts = db.session.query(BlogPost).all()
    requested_post = None
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)