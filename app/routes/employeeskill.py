from flask import jsonify, request, Blueprint
import app.db as db

routes = Blueprint('employee_skill_routes', __name__)


@routes.route("/employeeskills", methods=['POST'])
def saveOrUpdateEmployeeSkill():
    data = request.json
    e_skill = db.saveOrUpdateEmployeeSkill(data)
    return jsonify(e_skill.to_dict()), 200
