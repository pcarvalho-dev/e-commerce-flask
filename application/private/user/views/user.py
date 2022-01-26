from application.private.user import user_private_bp
from application.private.user.models.user import User
from application.private.user.schemas.user import UserSchema
from application.services.endpoints import default_return
from flask import request
from flask_jwt_extended import jwt_required


@user_private_bp.route("", methods=["GET", "POST"])
@jwt_required()
def item_views():
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
