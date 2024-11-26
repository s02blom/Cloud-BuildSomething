from flask import (Flask, Blueprint, render_template, request, redirect, url_for)
blueprint = Blueprint("main", __name__)

@blueprint.route('/', methods=['GET'])
def frontpage():
    lst = [[True, "Hello"], [False, "World"]]
    return render_template("view.j2", todo=lst)

@blueprint.route('/add', methods=['POST'])
def add():
    description = request.form.get("description")
    # Send request to backend
    return redirect(url_for("main.frontpage"), code=302)

@blueprint.route('/switch_status', methods=['POST'])
def switch_status():
    description = request.form.get("selected_task")
    # Send request to backend
    return redirect(url_for('main.frontpage'), code= 302)
