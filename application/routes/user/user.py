from application.controllers.user import create_user, read_users
from application.routes.user import user_bp
from application.services.request.requests import default_return
from flask_jwt_extended import jwt_required


@user_bp.post("")
def post_user():
    try:
        data = create_user()
        return default_return(201, 1, data)
    except Exception as e:
        raise e


@user_bp.get("")
@jwt_required()
def get_user():
    try:
        data = read_users()
        return default_return(200, 2, data)
    except Exception as e:
        raise e
