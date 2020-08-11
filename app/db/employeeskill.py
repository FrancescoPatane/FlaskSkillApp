from .models import EmployeeSkill
from .. import sqlAlchemy as db


def saveOrUpdateEmployeeSkill(data):
    emp_skill = EmployeeSkill(data['employee_id'], data['skill_name'], data['level'])
    db.session.merge(emp_skill)
    db.session.commit()
    return emp_skill
