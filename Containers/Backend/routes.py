from flask import (Flask, Blueprint, request, jsonify)
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
    description = request.get_json()
    sql_querie = """
    INSERT INTO ToDo (description) VALUES
    (%(description)s)
    """
    helper = {
        "description": description
    }
    print(f"{description=}")
    conn = db.get_connection(True)
    with conn.cursor() as cursor:
        cursor.execute(sql_querie, helper)
        cursor.fetchall()
    return jsonify(success=True)

@blueprint.route('/change_status', methods=['POST'])
def change_status():
    id = request.get_json()
    sql_get_item = """
    SELECT * FROM ToDo
    WHERE id = (%(description)s)
    """
    sql_update_status = """
    UPDATE ToDo
    SET status = (%(status)s)
    WHERE id = (%(id)s)
    """
    get_item_helper = {
        "description": id        
    }
    conn = db.get_connection(True)
    with conn.cursor() as cursor:
        cursor.execute(sql_get_item, get_item_helper)
        row = cursor.fetchall()
        update_status_helper = { 
            "status": not row[0][1],
            "id": row[0][0]
        }
        cursor.execute(sql_update_status, update_status_helper)
    return jsonify(success=True)