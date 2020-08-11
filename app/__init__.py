from flask import Flask
from .ext import sqlAlchemy
from app.routes import routes

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    sqlAlchemy.init_app(app)
    app.register_blueprint(routes)
    return app
