from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

CORS(app)


# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

# initializing data base with app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

from models import db, User
db.init_app(app)

# adding resources to endpoints

from controllers import LoginResource, RegisterResource, QuoteResource

api.add_resource(LoginResource, '/login')
api.add_resource(RegisterResource, '/register')
api.add_resource(QuoteResource, '/quotes', '/quotes/<quote_id>')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        admin = User.query.filter_by(email='admin@mad2.com').first()

        if not admin:
            admin = User(name='Admin', email='admin@mad2.com', password='12345678', role='admin')
            db.session.add(admin)
            db.session.commit()
            print("Admin created!\n email: admin@mad2.com, password: 12345678")

    app.run(debug=True)