from flask import jsonify, make_response
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from sqlalchemy import or_

from application.models.user.user import User
from application.routes.auth import bp
from application.services.exceptions import UnauthorizedError


@bp.route("/login", methods=["POST"])
def login():
    basic = request.headers.get("Authorization")
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    # if not basic:
    #     raise UnauthorizedError('Basic token missing')

    user = User.query.filter(or_(User.username == username,
                                 User.email == username),
                             User.deleted_at.is_(None),
                             User.status == 1).first()
    if not user:
        return make_response(jsonify("User not found"), 200)

    if user.check_password(password):
        access_token = create_access_token(identity=username)
        return make_response(jsonify(access_token), 200)


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
