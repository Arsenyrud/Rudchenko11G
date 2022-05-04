import hashlib
from datetime import datetime
from init import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(80), unique=True)
    reg_date = db.Column(db.DateTime)
    b_date = db.Column(db.DateTime)
    password = db.Column(db.String(256), unique=True, nullable=False)

    def validate(self, password):
        return self.password == hashlib.md5(password.encode('utf8')).hexdigest()

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    image = db.Column(db.String(80))
    desc = db.Column(db.String(200))

    def __repr__(self):
        return f'[{self.id}] {self.name}'


class Basket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    count = db.Column(db.Integer)


class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(400), nullable=False)
    time = db.Column(db.DateTime)

db.create_all()

if __name__ == '__main__':
    pass

db.session.commit()
