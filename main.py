import flask
import werkzeug
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html",logged_in=current_user.is_authenticated)


@app.route('/register',methods=['GET','POST'])
def register():

    if request.method=="POST":
        password=werkzeug.security.generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)
        new=User(

            email=request.form.get("email"),
            name=request.form.get("name"),
            password=password

        )
        mails=User.query.filter_by(email=request.form.get("email")).first()
        if mails:
            flash("user already exist")
        else:
            db.session.add(new)
            db.session.commit()
            login_user(new)
            return redirect(url_for('secrets',name=request.form.get("name")))
    return render_template("register.html",logged_in=current_user.is_authenticated)


@app.route('/login',methods=["GET","POST"])
def login():
    error=""
    if request.method=="POST":

        email=request.form.get("email")
        data=User.query.filter_by(email=email).first()
        if data:
            password=data.password
            compare= werkzeug.security.check_password_hash(password,request.form.get("password"))
            if compare:
                login_user(data)
                flash('successfully logged in')
                return redirect(url_for('secrets',name=data.name))

            elif compare==False:
                error=("Invalid password or email")
        else :
            error=("user doesn't exist")
    return render_template("login.html",error=error,logged_in=current_user.is_authenticated)


@app.route('/secrets',methods=["GET"])
@login_required
def secrets():
    name=request.args.get("name")
    return render_template("secrets.html",name=name,logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    return send_from_directory('static',
                               filename="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
