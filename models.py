from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy()

class User(UserMixin, db.Model):

    #User model
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

class UpdateUser( db.Model):

    #User model
    __tablename__ = "user_details"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    firstname = db.Column(db.String(25), nullable=False)
    lastname = db.Column(db.String(25), nullable=False)
    address = db.Column(db.String(25),  nullable=False)
    mobileno= db.Column(db.String(12), unique=True, nullable=False )

    def __init__(self, username, firstname,lastname,address,mobileno):
        self.username=username
        self.firstname=firstname
        self.lastname=lastname
        self.address=address
        self.mobileno=mobileno

    def __repr__(self):
        return f"This {self.name} has {self.memory_in_gb} GB of memory"
