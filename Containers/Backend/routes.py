from flask import (Flask, Blueprint, request)
from . import db
blueprint = Blueprint("main", __name__)

@blueprint.route('/todo', methods=['GET'])
def get_all():
    sql_querie = """
    SELECT * FROM ToDo;
    """
    conn = db.get_connection()
    with conn.cursor() as cursor:
        cursor.execute(sql_querie)
        todo = cursor.fetchall()
    return todo

@blueprint.route('/insert', methods=['POST'])
def insert():
    description = request.json("description")
    sql_querie = """
    INSERT INTO ToDo (description) VALUES
    (%(description)s)
    """
    conn = db.get_connection()
    with conn.cursor() as cursor:
        cursor.execute(sql_querie, description)
        cursor.fetchall()
    return 200

@blueprint.route('/change_status', methods=['POST'])
def change_status():
    description = request.json("selected_task")
    sql_get_item = """
    SELECT * FROM ToDo
    WHERE description = (%(description)s)
    """
    sql_update_status = """
    UPDATE ToDo
    SET status = (%(status)s)
    WHERE id = (%(id)s)
    """
    conn = db.get_connection()
    with conn.cursor() as cursor:
        cursor.execute(sql_get_item, description)
        row = cursor.fetchall()
        cursor.execute(sql_update_status, not row['status'], row['id'])
    return 200