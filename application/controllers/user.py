from application.schemas.user import UserSchema
from flask import request
from application.models.user import User


def read_users():
    users = User.query.all()
    return UserSchema(many=True).dump(users)


def create_user():
    request_body = request.get_json()
    data = User().create_object(request_body).save()
    return UserSchema().dump(data)
