from flask import jsonify, abort, request, Blueprint
import app.db as db

routes = Blueprint('employee_routes', __name__)


@routes.route("/employees")
def findAllEmployees():
    employees = db.findAllEmployees()
    data = list(map(lambda e: e.to_dict(), employees))
    return jsonify(data), 200

@routes.route("/employees/<email>")
def findEmployeeByEmail(email):
    employee = db.findEmployeeByEmail(email)
    return jsonify(employee.to_dict()), 200

@routes.route("/employees", methods=['POST'])
def addEmployee():
    data = request.json
    employee = db.saveOrUpdateEmployee(data)
    return jsonify(employee.to_dict()), 200
