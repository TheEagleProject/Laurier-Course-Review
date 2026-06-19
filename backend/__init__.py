from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from dotenv import load_dotenv


load_dotenv()
print("DATABASE_URL:", os.getenv('DATABASE_URL'))
print("SECRET_KEY:", os.getenv('SECRET_KEY'))


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    db.init_app(app)
    login_manager.init_app(app)
    with app.app_context():
        from backend.models.user import User
        from backend.models.course import Course
        from backend.models.professor import Professor
        from backend.models.review import Review
        db.create_all()
    return app


