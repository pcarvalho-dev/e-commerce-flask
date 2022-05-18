from flask import request
from application.models.user import User


def read_users():
    users = User.query.all()
    return users


def create_user(data):
    request_body = request.get_json()
    data = User().create_object(data).save()
    return data
