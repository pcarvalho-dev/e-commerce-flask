from crypt import methods
from application.private.product import product_private_bp
from application.private.product.models.product import Product
from application.private.product.schemas.product import ProductSchema
from application.private.product.models.product_like import ProductLike
from application.private.user.services.crud import get_user
from application.services.endpoints import default_return
from flask import request
from flask_jwt_extended import (get_jwt_identity,
                                jwt_required)


@product_private_bp.route("", methods=["GET"])
@jwt_required()
def get_all():
    try:
        if request.method == 'GET':
            products = Product.query.filter(Product.deleted_at.is_(
                None)).filter(Product.status.is_(True)).all()
            schema_product = ProductSchema(many=True).dump(products)
            return default_return(200, 2, schema_product)
    except Exception as e:
        raise e


@product_private_bp.route("/<id>", methods=['GET'])
@jwt_required()
def get_one(id):
    try:
        if request.method == 'GET':
            product = Product.get_by_id(id)
            schema_product = ProductSchema(many=False).dump(product)
            return default_return(200, 2, schema_product)
    except Exception as e:
        raise e


@product_private_bp.route("", methods=["POST"])
@jwt_required()
def create():
    try:
        if request.method == 'POST':
            request_body = request.get_json()
            item = Product().create_object(request_body).save()
            item = ProductSchema().dump(item)
            return default_return(201, 1, item)
    except Exception as e:
        raise e


@product_private_bp.route("/<id>", methods=["PUT", "PATCH"])
@jwt_required()
def update(id):
    try:
        item = Product().get_by_id(id)
        request_body = request.get_json()
        item.update_object(request_body).update()

        return default_return(201, 3, ProductSchema().dump(item))
    except Exception as e:
        raise e


@product_private_bp.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    try:
        if request.method == 'DELETE':
            item = Product().get_by_id(id)
            item.delete()

            return default_return(200, 4, ProductSchema().dump(item))
    except Exception as e:
        raise e


@product_private_bp.route("/<id>/like", methods=["POST"])
@jwt_required()
def like(id):
    try:
        if request.method == 'POST':
            user_jwt = get_jwt_identity()
            user = get_user(user_jwt['id'])
            ProductLike().create_object(
                dict_body={"user_id": int(user.id), "product_id": int(id), "deleted_at": None}).save()

            return default_return(201, 1, {})

    except Exception as e:
        raise e


@product_private_bp.route("/<id>/dislike", methods=["DELETE"])
@jwt_required()
def dislike(id):
    try:
        if request.method == 'DELETE':
            user_jwt = get_jwt_identity()
            user = get_user(user_jwt['id'])

            item = ProductLike.query.filter(ProductLike.product_id == id).filter(
                ProductLike.user_id == user.id).first()

            item.delete()

            return default_return(200, 4, {})

    except Exception as e:
        raise e
