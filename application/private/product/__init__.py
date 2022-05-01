from flask import Blueprint

product_private_bp = Blueprint("product_private_bp", __name__)

from .views import product


def init_app(app):
    app.register_blueprint(product_private_bp, url_prefix="/v1/private/product")
