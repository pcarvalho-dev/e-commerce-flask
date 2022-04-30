from flask import Blueprint

category_bp = Blueprint("category_bp", __name__)

from . import category


def init_app(app):
    app.register_blueprint(category_bp, url_prefix="/v1/category")
