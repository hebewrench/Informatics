from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, RadioField
from wtforms.validators import InputRequired, Length, Email, EqualTo




class search(FlaskForm):
    title = StringField()
    author = StringField()
    genre = StringField()
