from flask import Flask
from . import create_app

def register_blueprints(app):
    from . import routes
    print("Registering blueprints...")
    app.register_blueprint(routes.blueprint)
    # print("Registered blueprints:")
    # print(app.url_map)

app = create_app()
register_blueprints(app)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
