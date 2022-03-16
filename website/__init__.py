from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__) #"__name__" is the name of the file that was ran (always do that when initializing flask apps)
    app.config['SECRET_KEY'] = 'La Li Lu Le Lo' #Secures client-side sessions by encrypting cookies
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') #register_blueprint() makes the routes in views.py and auth.py recognized by the app
    app.register_blueprint(auth, url_prefix='/') #url_prefix = '/' means that we just need to type '/' before entering the name of a route in auth.py

    from .models import User, Note
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')