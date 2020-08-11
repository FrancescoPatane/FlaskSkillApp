from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from ..ext import sqlAlchemy as db


class Skill(db.Model):
    __tablename__ = 'skill'

    name = Column(String(25), primary_key=True)
    description = Column(String(255))

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def to_dict(self):
        data = {
            'name': self.name,
            'description': self.description
        }
        return data


class Employee(db.Model):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    surname = Column(String(25))
    email = Column(String(40))
    role = Column(String(40))


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
            'role': self.role
        }
        return data
