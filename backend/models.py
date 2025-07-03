from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False, default='user')

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'role': self.role
        }
    
class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(80), nullable=False)
    author_image = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'author': self.author,
            'author_image': self.author_image,
            'text': self.text
        }