from application.routes.tests import tests_bp


@tests_bp.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
