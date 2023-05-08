from flask import Blueprint, jsonify
from .controllers import get_all_vehicles, get_vehicle_by_id


vehicle_bp = Blueprint('vehicle', __name__, url_prefix='/vehicles')

@vehicle_bp.route('/', methods=['GET'])
def get_vehicles():
    return get_all_vehicles()

@vehicle_bp.route('/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):
    return get_vehicle_by_id(vehicle_id)