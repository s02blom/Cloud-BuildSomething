from flask import (Flask, Blueprint, render_template, request)
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


blueprint = Blueprint("main", __name__)

@blueprint.route('/', methods=['GET'])
def frontpage():
    lst = [[True, "Hello"], [False, "World"]]
    new_todo = New_todo()
    return render_template("view.j2", todo=lst, New_todo=new_todo)

@blueprint.route('/add', methods=['POST'])
def add(description):
    return "Hello, add"

@blueprint.route('/check', methods=['PATCH'])
def check(id):
    pass

@blueprint.route('/uncheck', methods=['PATCH'])
def uncheck(id):
    pass

@blueprint.route('/fetch', methods=['GET'])
def get():
    pass

class New_todo(FlaskForm):
    description = StringField("description", validators=[DataRequired()])