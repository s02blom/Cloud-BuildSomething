from flask import (Flask, Blueprint, request,)
blueprint = Blueprint("main", __name__)

@blueprint.route('/todo', methods=['GET'])
def get_all():
    sql_querie = """
    SELECT * FROM 
    """

@blueprint.route('/add', methods=['POST'])
def add():
    description = request.json("description")

@blueprint.route('/switch_status', methods=['POST'])
def switch_status():
    description = request.json("selected_task")
