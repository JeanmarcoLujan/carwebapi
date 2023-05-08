from flask import jsonify


# Lógica para obtener todos los vehículos
def get_all_vehicles():
    vehicles = [
        {'id': 1, 'brand': 'Toyota', 'model': 'Corolla'},
        {'id': 2, 'brand': 'Honda', 'model': 'Civic'}
    ]
    return jsonify(vehicles)

# Lógica para obtener un vehículo por ID
def get_vehicle_by_id(vehicle_id):
    vehicle = {'id': vehicle_id, 'brand': 'Toyota', 'model': 'Corolla'}
    return jsonify(vehicle)