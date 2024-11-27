from flask import (Flask, Blueprint, render_template, request, redirect, url_for)
import requests
import os
blueprint = Blueprint("main", __name__)

BACKEND_URL = f"http://{os.environ.get('BACKEND')}:{os.environ.get('BACKEND_PORT')}"

@blueprint.route('/', methods=['GET'])
def frontpage():
    todo = requests.get(url=f"{BACKEND_URL}/todo")
    print(type(todo))
    print(todo.json())
    return render_template("view.j2", todo=todo.json())

@blueprint.route('/add', methods=['POST'])
def add():
    description = request.form.get("description")
    retun_code = requests.post(url=f"{BACKEND_URL}/insert", json=description)
    return redirect(url_for("main.frontpage"), code=302)

@blueprint.route('/switch_status', methods=['POST'])
def switch_status():
    description = request.form.get("selected_task")
    retun_code = requests.post(url=f"{BACKEND_URL}/change_status", json=description)
    return redirect(url_for('main.frontpage'), code= 302)
