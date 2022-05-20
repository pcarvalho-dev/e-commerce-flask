from application.models.user import User
from application.schemas.user import UserSchema
from flask import request


def read_users():
    users = User.query.all()
    return UserSchema(many=True).dump(users)


def create_user():
    request_body = request.get_json()
    data = User().create_object(request_body).save()
    return UserSchema().dump(data)

def read_user(id: int) -> dict:
    user = User.query.filter_by(id=id, deleted_at=None).first()
    return UserSchema().dump(user)

def delete_user(id: int) -> dict:
    user = User.query.filter_by(id=id, deleted_at=None).first()
    user.delete()
    
