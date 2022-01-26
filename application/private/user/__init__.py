from flask import Blueprint

user_private_bp = Blueprint("user_private_bp", __name__)

from .views import user


def init_app(app):
    app.register_blueprint(user_private_bp, url_prefix="/v1/private/users")
