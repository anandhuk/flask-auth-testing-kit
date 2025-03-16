# import secrets
# import hashlib
# import base64
# from flask import Blueprint, request, jsonify
# from flask_jwt_extended import (
#     create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt
# )
# from app.models.user import User
# from app.models.revoked_token import RevokedToken
# from app.extensions import db

# auth_bp = Blueprint("auth", __name__)

# # Store PKCE verifiers temporarily
# pkce_verifiers = {}

# def generate_code_challenge(code_verifier):
#     hashed = hashlib.sha256(code_verifier.encode()).digest()
#     return base64.urlsafe_b64encode(hashed).decode().rstrip("=")

# @auth_bp.route("/authorize", methods=["GET"])
# def authorize():
#     client_id = request.args.get("client_id")
#     redirect_uri = request.args.get("redirect_uri")
#     code_verifier = secrets.token_urlsafe(64)
#     code_challenge = generate_code_challenge(code_verifier)
#     pkce_verifiers[client_id] = code_verifier
#     auth_code = secrets.token_urlsafe(32)
#     return jsonify({"auth_code": auth_code, "code_challenge": code_challenge})

# @auth_bp.route("/token", methods=["POST"])
# def token():
#     data = request.json
#     client_id = data.get("client_id")
#     code_verifier = data.get("code_verifier")

#     if pkce_verifiers.get(client_id) != code_verifier:
#         return jsonify({"error": "Invalid PKCE verifier"}), 400

#     user = User.query.first()
#     access_token = create_access_token(identity={"username": user.username, "role": user.role})
#     refresh_token = create_refresh_token(identity={"username": user.username})
#     return jsonify({"access_token": access_token, "refresh_token": refresh_token})

# @auth_bp.route("/logout", methods=["POST"])
# @jwt_required()
# def logout():
#     jti = get_jwt()["jti"]
#     revoked = RevokedToken(jti=jti)
#     db.session.add(revoked)
#     db.session.commit()
#     return jsonify({"message": "Token revoked"}), 200


# import base64
# from flask import Blueprint, request, jsonify
# from flask_jwt_extended import (
#     create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jwt
# )
# from werkzeug.security import check_password_hash
# from app.models.user import User
# from app.models.revoked_token import RevokedToken
# from app.extensions import db

# auth_bp = Blueprint("auth", __name__)

# @auth_bp.route("/token", methods=["POST"])
# def token():
    
#     data = request.json
#     client_id = data.get("client_id")
#     client_secret = data.get("client_secret")
#     grant_type = data.get("grant_type")
    
#     # Validate grant type
#     if grant_type != "password":
#         return jsonify({"error": "Unsupported grant type"}), 400

#     # Decode Base64 encoded credentials
#     try:
#         decoded_bytes = base64.b64decode(data.get("password"))
#         password = decoded_bytes.decode("utf-8")
#     except Exception:
#         return jsonify({"error": "Invalid password encoding"}), 400

#     # Validate user
#     user = User.query.filter_by(username=data.get("username")).first()
#     if not user or not check_password_hash(user.password_hash, password):
#         return jsonify({"error": "Invalid credentials"}), 401

#     # Generate tokens
#     access_token = create_access_token(identity={"username": user.username, "role": user.role})
#     refresh_token = create_refresh_token(identity={"username": user.username})

#     return jsonify({"access_token": access_token, "refresh_token": refresh_token})

# @auth_bp.route("/refresh", methods=["POST"])
# @jwt_required(refresh=True)
# def refresh():
#     current_user = get_jwt_identity()
#     new_access_token = create_access_token(identity=current_user)
#     return jsonify({"access_token": new_access_token})

# @auth_bp.route("/logout", methods=["POST"])
# @jwt_required()
# def logout():
#     jti = get_jwt()["jti"]
#     revoked = RevokedToken(jti=jti)
#     db.session.add(revoked)
#     db.session.commit()
#     return jsonify({"message": "Token revoked"}), 200

# @auth_bp.route("/user", methods=["GET"])
# @jwt_required()
# def get_user():
#     current_user = get_jwt_identity()  # Extract user identity from token
#     user = User.query.filter_by(username=current_user["username"]).first()

#     if not user:
#         return jsonify({"error": "User not found"}), 404

#     user_data = {
#         "id": user.id,
#         "username": user.username,
#         "role": user.role
#     }
#     return jsonify(user_data)