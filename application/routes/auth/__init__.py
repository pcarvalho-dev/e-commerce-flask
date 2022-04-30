from flask import Blueprint

auth_bp = Blueprint("login_bp", __name__)

from . import auth


def init_app(app):
    app.register_blueprint(auth_bp, url_prefix="/v1/auth")
