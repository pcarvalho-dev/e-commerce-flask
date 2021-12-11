from flask import Blueprint

bp = Blueprint("login_bp", __name__)

from . import auth

def init_app(app):
    app.register_blueprint(bp, url_prefix="/v1/auth")
