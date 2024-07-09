from . import db
from dataclasses import dataclass


@dataclass
class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    # owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<List {self.id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text
        }


@dataclass
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # lists = db.relationship('List', backref='owner', lazy=True)

    def __repr__(self):
        return f'<User {self.name}>'

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}

