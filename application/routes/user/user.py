from application.routes.user import user_bp
from application.routes.user.services.crud import read_users, create_user
from application.schemas.default import default_schema
from application.schemas.user import UserInputSchema, UserOutputSchema
from application.services.request.requests import default_return
from flask_jwt_extended import jwt_required


@user_bp.post("")
@user_bp.input(UserInputSchema)
@user_bp.output(default_schema(UserOutputSchema))
@user_bp.doc(
    summary='Create user',
    description='This method create a user',
    tags=['User']
)
@jwt_required()
def post_user(data):
    try:
        data = create_user(data)
        return default_return(201, 1, data)
    except Exception as e:
        raise e


@user_bp.get("")
@user_bp.output(default_schema(UserOutputSchema, many=True))
@user_bp.doc(
    summary='List all users',
    description='This method list all users in DB',
    tags=['User']
)
@jwt_required()
def get_user():
    try:
        data = read_users()
        return default_return(200, 2, data)
    except Exception as e:
        raise e
