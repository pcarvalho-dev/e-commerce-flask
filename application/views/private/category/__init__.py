from flask import Blueprint

category_private_bp = Blueprint("category_private_bp", __name__)

from . import category


def init_app(app):
    app.register_blueprint(category_private_bp, url_prefix="/v1/private/categories")
