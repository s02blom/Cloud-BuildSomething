from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def frontpage():
    return "Hello, world"

@app.route('/add', methods=['POST'])
def add(description):
    pass

@app.route('/check', methods=['PATCH'])
def check(id):
    pass

@app.route('/uncheck', methods=['PATCH'])
def uncheck(id):
    pass

@app.route('/fetch', methods=['GET'])
def get():
    pass

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


