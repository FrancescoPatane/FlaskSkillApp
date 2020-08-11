from .models import *
from .. import sqlAlchemy as db

def findAllSkills():
    data = Skill.query.all()
    return data



def findSkill(skill):
    data = Skill.query.filter_by(name=skill).first()
    return data

def saveOrUpdateSkill(data):
    skill = Skill(data['name'], data['description'])
    db.session.merge(skill)
    db.session.commit()
    return skill
