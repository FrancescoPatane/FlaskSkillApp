from .models import Skill
from .. import sqlAlchemy as db

def findAllSkills():
    data = Skill.query.all()
    return data



def findSkill(skill):
    data = Skill.query.filter_by(name=skill).first()
    return data

def findSkillWithEmployess(skill):
    query = "select e.name, e.surname, e.email, e.role, es.level from skill s join employee_skill es on s.name = es.skill_name join employee e on e.id = es.employee_id where s.name = :skill"
    data = db.session.execute(query, {'skill': skill});
    rows = data.fetchall()
    if len(rows) > 0:
        return [dict(row) for row in rows]
    else:
        return rows


def saveOrUpdateSkill(data):
    skill = Skill(data['name'], data['description'])
    db.session.merge(skill)
    db.session.commit()
    return skill
