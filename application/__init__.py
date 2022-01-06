from flask import Flask

from application.services.date_and_time import get_now
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

    from application.views import auth
    auth.init_app(app)

    from application.views.private import user
    user.init_app(app)
    from application.views.private import group
    group.init_app(app)
    from application.views.private import category
    category.init_app(app)

    return app
