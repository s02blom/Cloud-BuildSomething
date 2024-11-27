from flask import Flask
from . import create_app
import db

def register_blueprints(app):
    from . import routes
    print("Registering blueprints...")
    app.register_blueprint(routes.blueprint)



app = create_app()
register_blueprints(app)
db.init_database()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
