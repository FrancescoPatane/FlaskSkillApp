from . import dbconnection
from .models import *
from .. import sqlAlchemy as db

def findAllSkills():
    # conn = dbconnection.connection()
    # cursor = conn.cursor()
    # cursor.execute("SELECT * FROM SKILL")
    # data = cursor.fetchall()
    data = Skill.query.all()
    print(data)
    return data



def findSkill(skill):
    # conn = dbconnection.connection()
    # cursor = conn.cursor()
    # query = "SELECT * FROM SKILL WHERE name = %s"
    # params = (skill,)
    # cursor.execute(query, params)
    # data = cursor.fetchone()
    data = Skill.query.filter_by(name=skill).first()
    print (data.name)
    return data
