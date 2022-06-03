from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL,Email

from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    email=StringField("Email",validators=[DataRequired(),Email()])
    name=StringField("name",validators=[DataRequired()])
    password=PasswordField("password",validators=[DataRequired()])
    submit=SubmitField("submit")

class LoginForm(FlaskForm):
    email=StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("submit")

class CommentForm(FlaskForm):
    body = CKEditorField("Enter your opinion", validators=[DataRequired()])
    submit = SubmitField("Submit Post")