from __main__ import app, db

from flask_bcrypt import Bcrypt

# db = SQLAlchemy()
# bcrypt = Bcrypt()



# db = SQLAlchemy()

class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(25), unique=True, nullable=True)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return f"<Register(id={self.id}, email='{self.email}', UserName='{self.UserName}')>"

    def to_dict(self):
        return {
            'id': self.id,
            'UserName': self.UserName,
            'email': self.email
        }
