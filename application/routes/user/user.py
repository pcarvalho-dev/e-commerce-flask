from application.models.user import User
from application.routes.user import user_bp
from application.schemas.user import UserSchema
from application.services.request.requests import default_return
from flask import request
from flask_jwt_extended import jwt_required


@user_bp.route("", methods=["POST"])
@user_bp.output(UserSchema())
@jwt_required()
def create_user():
    try:
        request_body = request.get_json()
        item = User().create_object(request_body).save()
        item = UserSchema().dump(item)
        return default_return(201, 1, item)
    except Exception as e:
        raise e


@user_bp.route("", methods=["GET"])
@user_bp.input(UserSchema())  # Request body
@user_bp.output(UserSchema())  # Response body
@jwt_required()
def list_user():
    try:
        return "ok"
    except Exception as e:
        raise e
