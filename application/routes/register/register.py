from application.private.user.schemas.user import UserSchema
from application.private.user.models.user import User
from application.public.register import register_bp
from application.services.endpoints import default_return
from application.services.exceptions import UnauthorizedError
from flask import jsonify, make_response, request
from flask_jwt_extended import (create_access_token, get_jwt_identity,
                                jwt_required)
from sqlalchemy import or_

@register_bp.route("", methods=["POST"])
def register():
    try:
        if request.method == 'POST':
            request_body = request.get_json()
            item = User().create_object(request_body).save()
            item = UserSchema().dump(item)
            return default_return(201, 1, item)
    except Exception as e:
        raise e
