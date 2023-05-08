from flask import Blueprint, jsonify
from .controllers import get_all_users, get_user_by_id

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
def get_users():
    return get_all_users()

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return get_user_by_id(user_id)