from flask import Flask
from flask_sqlalchemy import SQLAlchemy

sqlAlchemy = SQLAlchemy()


def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    #app.config.from_object(config_class)

    sqlAlchemy.init_app(app)
    app.register_blueprint(routes)
    return app

from app.routes import routes
