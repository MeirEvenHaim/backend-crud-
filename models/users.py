from __main__ import app, db

from flask_bcrypt import *


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(25), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    img = db.Column(db.String(100))

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}', img='{self.img}')>"

    def to_dict(self):
        return {
            'id': self.id,
            'UserName': self.UserName,
            'email': self.email,
            'password': self.password,
            'address': self.address,
            'img': self.img
        }

    def set_password(self, password):
        self.password = generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return check_password_hash(self.password, password)
