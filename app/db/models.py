from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from ..ext import sqlAlchemy as db


class Skill(db.Model):
    __tablename__ = 'skill'

    name = Column(String(25), primary_key=True)
    description = Column(String(255))

    def to_dict(self):
        data = {
            'name': self.name,
            'description': self.description
        }
        return data
