from flask import jsonify
from . import routes
import app.db as db

@routes.route('/users')
def users():
    return render_template('users.html')


@routes.route("/skills")
def findAllSkills():
    skills = db.findAllSkills()
    data = list(map(lambda s: s.to_dict(), skills))
    return jsonify(data), 200

@routes.route("/skills/<skill>")
def findSkill(skill):
    skill = db.findSkill(skill)
    return jsonify(skill.to_dict()), 200
