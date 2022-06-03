from functools import wraps
import werkzeug
from flask import Flask, render_template, redirect, url_for, flash, request,abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date

from flask_gravatar import Gravatar
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship,backref
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm, RegisterForm,LoginForm,CommentForm
from flask_gravatar import Gravatar

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
#gravatar config
gravatar = Gravatar(app, size=100, rating='g', default='retro', force_default=False, force_lower=False, use_ssl=False, base_url=None)


##CONFIGURE TABLES

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(250), nullable=False)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


class User(UserMixin,db.Model):
    __tablename__ = "User"
    comments = relationship("Comment",back_populates="user")
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

class Comment(db.Model):
    __tablename__ = "Comment"
    body= db.Column(db.String(1000))
    id = db.Column(db.Integer, primary_key=True)
    auth_id = db.Column(db.Integer, ForeignKey('User.id'))
    user=relationship("User",back_populates="comments")

login_manager=LoginManager()
login_manager.init_app(app)
db.create_all()
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        #If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        #Otherwise continue with the route function
        return f(*args, **kwargs)
    return decorated_function


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts,logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST":
        password=werkzeug.security.generate_password_hash(password=form.password.data, method='pbkdf2:sha256',
                                                 salt_length=8)
        new = User(

            email=form.email.data,
            name=form.name.data,
            password=password

        )
        mails = User.query.filter_by(email=request.form.get("email")).first()
        if mails:
            flash("user already exist")
        else:
            db.session.add(new)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template("register.html", form=form,logged_in=current_user.is_authenticated)


@app.route('/login',methods=["GET","POST"])
def login():
    form=LoginForm()
    if request.method=="POST":
        email=form.email.data
        user=User.query.filter_by(email=email).first()
        if user:
            password=user.password
            compare = werkzeug.security.check_password_hash(password, form.password.data)
            if compare:
               login_user(user)
               return redirect(url_for('get_all_posts'))
            elif compare==False:
               flash("error:invalid password or email id")
               return redirect(url_for('login'))
        else:
            flash("error:youre not registered...pls register first")
            return redirect(url_for('register'))
    return render_template("login.html",form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>",methods=["GET","POST"])
@login_required
def show_post(post_id):
    form=CommentForm()
    requested_post = BlogPost.query.get(post_id)

    if request.method=="POST":
            new = Comment(
                auth_id=post_id,
                body=form.body.data
            )
            db.session.add(new)
            db.session.commit()
            comment = Comment.query.all()
            return redirect(url_for('show_post',post_id=post_id,comment=comments,post=requested_post,logged_in=current_user.is_authenticated,form=form))
    comments = Comment.query.all()
    return render_template("post.html",comment=comments, post=requested_post,logged_in=current_user.is_authenticated,form=form)





@app.route("/about")
@login_required
def about():
    return render_template("about.html",logged_in=current_user.is_authenticated)


@app.route("/contact")
@login_required
def contact():
    return render_template("contact.html",logged_in=current_user.is_authenticated)


@app.route("/new-post",methods=["GET","POST"])
@admin_only
@login_required
def add_new_post():
    form = CreatePostForm()
    if request.method=="POST":
        new_post = BlogPost(

            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user.id,

            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form,logged_in=current_user.is_authenticated)


@app.route("/edit-post/<int:post_id>")
@login_required
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)


@app.route("/delete/<int:post_id>")
@admin_only
@login_required
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(debug=True)
