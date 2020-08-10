from flask import current_app
import mysql.connector


def connection():
    connection = mysql.connector.connect(
      host=current_app.config['DB_HOST'],
      user=current_app.config['DB_USER'],
      password=current_app.config['DB_PASSWORD'],
      database=current_app.config['DB_DATABASE']
    )
    return connection
