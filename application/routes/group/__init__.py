from flask import Blueprint

group_bp = Blueprint("group_bp", __name__)

from . import group


def init_app(app):
    app.register_blueprint(group_bp, url_prefix="/v1/group")
