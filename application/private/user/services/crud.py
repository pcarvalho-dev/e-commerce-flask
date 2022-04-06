
from application.private.user.models.user import User
from application.private.user.schemas.user import UserSchema
from application.services.exceptions import NotFoundError


def get_user(id):
    query = User.query.filter(User.deleted_at == None)

    try:
        int(id)
        item = query.filter(User.id == id).first()
    except:
        item = query.filter(User.username == id).first()

    if not item:
        raise NotFoundError()
    
    return item