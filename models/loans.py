from __main__ import db
from datetime import datetime
from datetime import datetime
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('loans', lazy=True))
    admin = db.relationship('Admin', backref=db.backref('loans', lazy=True))
    book = db.relationship('Book', backref=db.backref('loans', lazy=True))

    def __repr__(self):
        return f"<Loan(id={self.id}, loan_date='{self.loan_date}', user_id={self.user_id}, user_name='{self.user.UserName}', admin_id={self.admin_id}, admin_name='{self.admin.UserName}', book_id={self.book_id}, book_name='{self.book.book_name}')>"

    def to_dict(self):
        return {
            'id': self.id,
            'loan_date': self.loan_date.isoformat(),
            'user_id': self.user_id,
            'user_name': self.user.UserName,
            'admin_id': self.admin_id,
            'admin_name': self.admin.UserName,
            'book_id': self.book_id,
            'book_name': self.book.book_name
        }
