from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token, create_refresh_token, jwt_required, get_jwt, get_jwt_identity
)
from werkzeug.security import check_password_hash
from app.models.user import User
from app.models.revoked_token import RevokedToken
from app.extensions import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/authorize", methods=["POST"])
def authorize():
    """Authenticate user and return JWT tokens."""
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # Find user by username
    user = User.query.filter_by(username=username).first()
    print(user.password_hash)
    print(password)
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid username or password"}), 401

    # Create JWT access & refresh tokens
    access_token = create_access_token(identity=user.username)
    refresh_token = create_refresh_token(identity=user.username)

    return jsonify({"access_token": access_token, "refresh_token": refresh_token}), 200

@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    """Revoke JWT token."""
    jti = get_jwt()["jti"]
    revoked = RevokedToken(jti=jti)
    db.session.add(revoked)
    db.session.commit()
    return jsonify({"message": "Token revoked"}), 200



@auth_bp.route("/user", methods=["GET"])
@jwt_required()
def get_user():
    current_username = get_jwt_identity()  
    user = User.query.filter_by(username=current_username).first()

    print(user.username)
    if not user:
        return jsonify({"error": "User not found"}), 404

    user_data = {
        "id": user.id,
        "username": user.username,
        "role": user.role
    }
    return jsonify(user_data)