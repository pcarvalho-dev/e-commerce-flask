from application.models.category import Category
from application.routes.category import category_bp
from application.schemas.category import CategorySchema
from application.services.endpoints import default_return
from flask import request
from flask_jwt_extended import jwt_required


@category_bp.route("", methods=["GET", "POST"])
@jwt_required()
def item_views():
    try:
        if request.method == 'GET':
            return "ok"
        if request.method == 'POST':
            request_body = request.get_json()
            item = Category().create_object(request_body).save()
            item = CategorySchema().dump(item)
            return default_return(201, 1, item)
    except Exception as e:
        raise e
