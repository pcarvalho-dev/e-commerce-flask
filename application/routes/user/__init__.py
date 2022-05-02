from apiflask import APIBlueprint

user_bp = APIBlueprint("user_bp", __name__)

from . import user


def init_app(app):
    app.register_blueprint(user_bp, url_prefix="/v1/users")
