from app import db
from app import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


#EXAMPLE FROM OTHER MODULE
""" class User(UserMixin, db.Model):
    userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.Text, nullable=False)
    lastname = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=True)
    passwordHash = db.Column(db.Text, nullable=True)
    accountType = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User('{self.firstname}','{self.email}')"

    def get_id(self):
        return self.userId

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.passwordHash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.passwordHash, password) """

