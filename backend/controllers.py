from flask_restful import Resource
from flask import request

from models import db, User

class HelloWorld(Resource):
    def get(self):
        users = User.query.all()
        users = [ user.to_dict() for user in users ]
        return {'message': 'Fetched all users', 'users': users}
    def post(self):
        data = request.get_json()
        name = data.get('name', None); email = data.get('email', None); password = data.get('password', None)
        if not name or not email or not password:
            return {'message': "Please provide all the required information!"}, 400
        user = User.query.filter_by(email=email).first()
        if user:
            return {'message': "User exists with provided email!"}, 400
        user = User(name=name, email=email, password=password)
        db.session.add(user); db.session.commit()
        return {'message': "User created!"}
    def put(self):
        data = request.get_json()
        name = data.get('name', None); email = data.get('email', None); password = data.get('password', None)
        if not name or not email or not password:
            return {'message': "Please provide all the required information!"}, 400
        user = User.query.filter_by(email=email).first()
        if not user:
            return {'message': "User doesnt' exists to update!"}, 400
        user.name = name
        user.email = email
        user.password = password
        db.session.commit()
        return {'message': "User updated!"}
    def delete(self):
        data = request.get_json()
        email = data.get('email', None)
        if not email:
            return {'message': "Please provide all the required information!"}, 400
        user = User.query.filter_by(email=email).first()
        if not user:
            return {'message': "User doesnt' exists to delete!"}, 400
        db.session.delete(user)
        db.session.commit()
        return {'message': "User deleted successfully!"}, 200