from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

protected_bp = Blueprint("protected", __name__)

@protected_bp.route("/user-data", methods=["GET"])
@jwt_required()
def user_data():
    current_user = get_jwt_identity()
    return jsonify({"message": f"User data accessed by {current_user['username']}"})