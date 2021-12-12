from flask import request

from application.models.group.group import Group
from application.routes.user.private import bp
from application.schemas.group.group import GroupSchema
from application.services.endpoints import default_return


@bp.route("", methods=["GET", "POST"])
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
