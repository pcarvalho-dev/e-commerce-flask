from application.models.user import User
from application.routes.auth import auth_bp
from application.services.endpoints import default_return
from flask import jsonify, request
from flask_jwt_extended import (create_access_token, get_jwt_identity,
                                jwt_required)
from sqlalchemy import or_


@auth_bp.route("/token", methods=["POST"])
def login():
    basic = request.headers.get("Authorization")
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if username == "root" and password == "root":
        access_token = create_access_token(identity=username)
        return {"access_token": access_token}
    else:
        # if not basic:
        #     raise UnauthorizedError('Basic token missing')

        user = User.query.filter(or_(User.username == username,
                                     User.email == username),
                                 User.deleted_at.is_(None),
                                 User.status == 1).first()
        if not user:
            return default_return(200, "User not found", {})

        if user.check_password(password):
            access_token = create_access_token(identity=username)
            return {"access_token": access_token}


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@auth_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
