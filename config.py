from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from flask_login import LoginManager
from flask_admin import Admin
from flask_basicauth import BasicAuth

app = Flask(__name__)
SECRET_KEY = b'\x00\xe3\xc9{\xc7|*\x13S\xfd\x18\x87nS/7\x80\xfa\x8e\xd499\xc7Z\xcc\xa7:n}[\xb9\x16'
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://c1933159:bingobangobongus123INFO@csmysql.cs.cf.ac.uk:3306/c1933159_informatics'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
admin = Admin(app)
basic_auth = BasicAuth(app)

@login_manager.user_loader
def load_user(user):
    return User.get(user)
