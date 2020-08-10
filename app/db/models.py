from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from .. import sqlAlchemy as db

Base = declarative_base()

class Skill(db.Model):
    __tablename__ = 'skill'
    name = Column(String(25), primary_key=True)
    description = Column(String(255))
