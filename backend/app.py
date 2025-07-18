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

from controllers import cache, LoginResource, RegisterResource, QuoteResource, ReportGenerate, GraphResource

api.add_resource(LoginResource, '/login')
api.add_resource(RegisterResource, '/register')
api.add_resource(QuoteResource, '/quotes', '/quotes/<quote_id>')
api.add_resource(ReportGenerate, '/generate_report')
api.add_resource(GraphResource, '/graph')

# initalize cache
app.config['CACHE_TYPE'] = 'RedisCache'
app.config['CACHE_REDIS_URL'] = 'redis://localhost:6379/0'
cache.init_app(app)

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