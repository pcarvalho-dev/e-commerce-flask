from application.private.product import product_private_bp
from application.private.product.models.product import Product
from application.private.product.schemas.product import ProductSchema
from application.services.endpoints import default_return
from flask import request
from flask_jwt_extended import jwt_required


@product_private_bp.route("", methods=["GET", "POST"])
@jwt_required()
def item_views():
    try:
        if request.method == 'GET':
            products = Product.query.filter(Product.deleted_at.is_(None)).all()
            schema_product = ProductSchema(many=True).dump(products)
            return default_return(200, 2, schema_product)
    except Exception as e:
        raise e
