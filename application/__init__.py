from flask import Flask
from extensions import cors, jwt, db, ma, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Extensions
    cors.init_app(app, resources={r"/*": {"origins": "*"}})
    jwt.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    @app.route("/", methods=["GET"])
    def index():
        return "ok", 200

    from application import routes
    routes.register_routes(app)

    return app
