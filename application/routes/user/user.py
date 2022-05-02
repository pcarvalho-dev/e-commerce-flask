from application.models.user import User
from application.routes.user import user_bp
from application.schemas.user import UserSchema
from application.services.request.requests import default_return
from flask import request
from flask_jwt_extended import jwt_required


@user_bp.route("", methods=["GET", "POST"])
@user_bp.output(UserSchema())
@jwt_required()
def create_user():
    try:
        if request.method == 'GET':
            return "ok"
        if request.method == 'POST':
            request_body = request.get_json()
            item = User().create_object(request_body).save()
            item = UserSchema().dump(item)
            return default_return(201, 1, item)
    except Exception as e:
        raise e
