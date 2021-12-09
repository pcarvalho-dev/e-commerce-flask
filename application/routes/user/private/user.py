from flask import request
from flask_jwt_extended import jwt_required

from application.models.user.user import User
from application.routes.user.private import bp
from application.schemas.user.user import UserSchema
from application.services.endpoints import default_return


@bp.route("", methods=["GET", "POST"])
def item_views():
    try:
        if request.method == 'GET':
            return "ok"
        if request.method == 'POST':
            request_body = request.get_json()
            item = User().create_item(request_body).save()
            item = UserSchema().dump(item)
            return default_return(201, 1, item)
    except Exception as e:
        raise e
