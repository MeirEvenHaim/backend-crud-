from __main__ import app, db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from datetime import datetime
from flask_bcrypt import Bcrypt

# db = SQLAlchemy()
# bcrypt = Bcrypt()
# from flask_bcrypt import *

# db = SQLAlchemy()

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(25), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    authorety_level = db.Column(db.Integer, nullable=False)
    img = db.Column(db.String(100))

    def __repr__(self):
        return f"<Admin(id={self.id}, email='{self.email}', authorety_level='{self.authorety_level}', img='{self.img}')>"

    def to_dict(self):
        return {
            'id': self.id,
            'UserName': self.UserName,
            'email': self.email,
            'address': self.address,
            'authorety_level': self.authorety_level,
            'img': self.img
        }

    def set_password(self, password):
        self.password = Bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return Bcrypt.check_password_hash(self.password, password)