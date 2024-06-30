from __main__ import app, db

class Employe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(25), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=False, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=False)
    img = db.Column(db.String(), unique=False)
    expertees = db.Column(db.String(30), unique=False, nullable=False)

    def __repr__(self):
        return f"<Employe(id={self.id}, email='{self.email}', img='{self.img}')>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'UserName': self.UserName,
            'email': self.email,
            'address': self.address,
            'img': self.img,
            'expertees': self.expertees
        }
