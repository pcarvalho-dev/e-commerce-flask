from flask import Blueprint

teste_bp = Blueprint("teste_bp", __name__)

from . import category


def init_app(app):
    app.register_blueprint(teste_bp, url_prefix="/v1/teste")
