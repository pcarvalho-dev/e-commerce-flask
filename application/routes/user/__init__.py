from flask import Blueprint

user_bp = Blueprint("user_bp", __name__)

from . import user


def init_app(app):
    app.register_blueprint(user_bp, url_prefix="/v1/user")
