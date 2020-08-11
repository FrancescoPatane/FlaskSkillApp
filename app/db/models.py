from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..ext import sqlAlchemy as db


class Skill(db.Model):
    __tablename__ = 'skill'

    name = Column(String(25), primary_key=True)
    description = Column(String(255))
    employees = relationship('EmployeeSkill', backref='skill', lazy=True)


    def __init__(self, name, description):
        self.name = name
        self.description = description

    def to_dict(self):
        data = {
            'name': self.name,
            'description': self.description,
            'employees': list(map(lambda es: es.to_dict(), self.employees))
        }
        return data


class Employee(db.Model):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    surname = Column(String(25))
    email = Column(String(40))
    role = Column(String(40))
    skills = relationship('EmployeeSkill', backref='employee', lazy=True)


    # def __init__(self, name, surname, email, role):
    #     self.name = name
    #     self.surname = surname
    #     self.email = email
    #     self.role = role

    def to_dict(self):
        data = {
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'role': self.role,
            'skills': list(map(lambda es: es.to_dict(), self.skills))
        }
        return data


class EmployeeSkill(db.Model):
    __tablename__ = 'employee_skill'

    employee_id = Column(Integer, ForeignKey('employee.id'), primary_key=True, nullable=False)
    skill_name = Column(String(25), ForeignKey('skill.name'), primary_key=True, nullable=False)
    level = Column(String(10))

    def __init__(self, employee_id, skill_name, level):
        self.employee_id = employee_id
        self.skill_name = skill_name
        self.level = level

    def to_dict(self):
        data = {
            'employee_id': self.employee_id,
            'skill_name': self.skill_name,
            'level': self.level
        }
        return data
