from flask import Blueprint

bp = Blueprint("group_bp", __name__)

from . import group


def init_app(app):
    app.register_blueprint(bp, url_prefix="/v1/private/groups")
