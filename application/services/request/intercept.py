from functools import wraps

from flask_jwt_extended import get_jwt_identity

from application.services.exceptions import UnauthorizedError


def intercept_admin_user(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        jwt_group_id = get_jwt_identity()['group_id']

        if jwt_group_id == 5:
            raise UnauthorizedError('Usuário não autorizado!')

        return f(*args, **kwargs)

    return wrap
