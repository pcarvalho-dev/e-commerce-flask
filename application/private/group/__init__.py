from flask import Blueprint

group_private_bp = Blueprint("group_private_bp", __name__)

from .views import group


def init_app(app):
    app.register_blueprint(group_private_bp, url_prefix="/v1/private/groups")
