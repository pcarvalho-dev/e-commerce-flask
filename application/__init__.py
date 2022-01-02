from flask import Flask

from application.services.date_and_time import get_now
from config import Config
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

    from application.routes import auth
    auth.init_app(app)

    from application.routes.user import private
    private.init_app(app)

    from application.routes.group import private
    private.init_app(app)

    return app
