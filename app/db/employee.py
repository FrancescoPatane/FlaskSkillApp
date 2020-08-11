from .models import Employee
from .. import sqlAlchemy as db

def findAllEmployees():
    data = Employee.query.all()
    return data



def findEmployeeByEmail(email):
    data = Employee.query.filter_by(email=email).first()
    return data

def saveOrUpdateEmployee(data):
    employee = findEmployeeByEmail(data['email'])
    if employee is None:
        employee = Employee()
    employee.name =  data['name']
    employee.surname =  data['surname']
    employee.email =  data['email']
    employee.role =  data['role']
    db.session.add(employee)
    db.session.commit()
    return employee
