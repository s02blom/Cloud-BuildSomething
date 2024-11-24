from flask import Flask

print("Debug print")
app = Flask(__name__)

def register_blueprints(app):
    from . import routes
    print("Registering blueprints...")
    app.register_blueprint(routes.blueprint)
    print("Registered blueprints:")
    print(app.url_map)
    # app.add_url_rule('/', endpoint="index")

register_blueprints(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
    # register_blueprints(app)

