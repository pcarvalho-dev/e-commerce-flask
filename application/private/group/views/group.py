from application.private.group import group_private_bp
from application.private.group.models.group import Group
from application.private.group.schemas.group import GroupSchema
from application.services.endpoints import default_return
from flask import request
from flask_jwt_extended import jwt_required


@group_private_bp.route("", methods=["GET", "POST"])
@jwt_required()
def item_views():
    try:
        if request.method == 'GET':
            return "ok"
        if request.method == 'POST':
            request_body = request.get_json()
            item = Group().create_object(request_body).save()
            item = GroupSchema().dump(item)
            return default_return(201, 1, item)
    except Exception as e:
        raise e
