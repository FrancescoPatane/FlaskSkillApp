from flask import jsonify, request
from . import routes
import app.db as db


@routes.route("/employeeskills", methods=['POST'])
def saveOrUpdateEmployeeSkill():
    data = request.json
    e_skill = db.saveOrUpdateEmployeeSkill(data)
    return jsonify(e_skill.to_dict()), 200
