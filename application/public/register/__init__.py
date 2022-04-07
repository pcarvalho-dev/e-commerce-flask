from flask import Blueprint

register_bp = Blueprint("register_bp", __name__)

from . import register

def init_app(app):
    app.register_blueprint(register_bp, url_prefix="/v1/register")
