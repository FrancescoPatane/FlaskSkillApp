from . import dbconnection

def findAllSkills():
    conn = dbconnection.connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM SKILL")
    data = cursor.fetchall()
    return data
