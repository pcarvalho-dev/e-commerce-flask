from flask import Flask
from extensions import cors, jwt, db, ma


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Extensions
    cors.init_app(app, resources={r"/*": {"origins": "*"}})
    jwt.init_app(app)
    db.init_app(app)
    ma.init_app(app)

    return app
