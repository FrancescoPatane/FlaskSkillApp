from flask import jsonify, abort, request
from . import routes
import app.db as db


@routes.route("/employees")
def findAllEmployees():
    employees = db.findAllEmployees()
    data = list(map(lambda e: e.to_dict(), employees))
    return jsonify(data), 200

@routes.route("/employees/<email>")
def findEmployee(email):
    employee = db.findEmployeeByEmail(email)
    return jsonify(employee.to_dict()), 200

@routes.route("/employees", methods=['POST'])
def addEmployee():
    data = request.json
    employee = db.saveOrUpdateEmployee(data)
    return jsonify(employee.to_dict()), 200
