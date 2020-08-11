from flask import Flask
from .ext import sqlAlchemy
from app.routes.skill import routes as skill_routes
from app.routes.employee import routes as employee_routes
from app.routes.employeeskill import routes as employee_skill_routes

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    sqlAlchemy.init_app(app)
    app.register_blueprint(skill_routes)
    app.register_blueprint(employee_routes)
    app.register_blueprint(employee_skill_routes)
    return app
