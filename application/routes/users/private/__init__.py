from flask import Blueprint

bp = Blueprint("user_bp", __name__)

from . import user

def init_app(app):
    app.register_blueprint(bp, url_prefix="/v1/private/users")
