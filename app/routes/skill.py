from flask import jsonify
from . import routes
import app.db as db

@routes.route('/users')
def users():
    return render_template('users.html')


@routes.route("/skills")
def findAllSkills():
    data = db.findAllSkills()
    return jsonify(data), 200
