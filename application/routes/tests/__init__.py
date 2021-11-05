from flask import Blueprint

tests_bp = Blueprint("tests", __name__,
                     url_prefix="/v1/tests")
from . import views


def init_app(app):
    app.register_blueprint(tests_bp)
