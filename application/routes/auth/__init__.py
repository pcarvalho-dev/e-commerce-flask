from apiflask import APIBlueprint

auth_bp = APIBlueprint("login", __name__)

from . import auth


def init_app(app):
    app.register_blueprint(auth_bp, url_prefix="/v1/auth")
