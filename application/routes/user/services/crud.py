from application.models.user import User


def read_users():
    users = User.query.all()
    return users


def create_user(data):
    data = User().create_object(data).save()
    return data
