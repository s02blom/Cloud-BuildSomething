from flask import (Flask, Blueprint, render_template, request)

blueprint = Blueprint("main", __name__)

@blueprint.route('/', methods=['GET'])
def frontpage():
    lst = []
    return render_template("view", todo=lst)

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
