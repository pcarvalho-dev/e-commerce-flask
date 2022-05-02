from application.models.user import User
from application.routes.user import user_bp
from application.schemas.user import UserOutputSchema, UserInputSchema
from application.services.request.requests import default_return
from flask import request
from flask_jwt_extended import jwt_required


@user_bp.post("")
@user_bp.output(UserOutputSchema)
@jwt_required()
def create_user():
    try:
        request_body = request.get_json()
        item = User().create_object(request_body).save()
        item = UserOutputSchema().dump(item)
        return default_return(201, 1, item)
    except Exception as e:
        raise e


@user_bp.get("")
@user_bp.doc(summary='List all users', description='This method list all users in DB', tags=['User'])
@user_bp.input(UserInputSchema)  # Request body
@user_bp.output(UserOutputSchema)  # Response body
# @user_bp.auth_required(auth_type='jwt')
@jwt_required()
def list_user():
    try:
        item = User.query.all()
        item = UserOutputSchema().dump(item)
        return default_return(200, 1, item)
    except Exception as e:
        raise e
