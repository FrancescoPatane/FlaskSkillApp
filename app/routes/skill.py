from flask import jsonify, abort, request, Blueprint
import app.db as db


routes = Blueprint('skill_routes', __name__)




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

@routes.route("/skills", methods=['POST'])
def addSkill():
    data = request.json
    skill = db.saveOrUpdateSkill(data)
    return jsonify(skill.to_dict()), 200
