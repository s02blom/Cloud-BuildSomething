from flask import Flask
from . import create_app
from . import db
from . import routes

def register_blueprints(app):
    from . import routes
    print("Registering blueprints...")
    app.register_blueprint(routes.blueprint)

app = create_app()
register_blueprints(app)
db.init_database()

print(routes.get_all())
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
