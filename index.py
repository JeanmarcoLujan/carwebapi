from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)

# Configuración de la conexión a MongoDB
app.config['MONGO_URI'] = 'mongodb+srv://jean:jean001@cluster0.dt3yttw.mongodb.net/carwash?retryWrites=true&w=majority'
mongo = PyMongo(app)

# Ruta para obtener todos los vehículos
@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = mongo.db.vehicles.find()
    response = []
    for vehicle in vehicles:
        response.append({
            'id': str(vehicle['_id']),
            'marca': vehicle['marca'],
            'anio': vehicle['anio']
        })
    return jsonify(response)

# Ruta para obtener un vehículo por ID
@app.route('/vehicles/<id>', methods=['GET'])
def get_vehicle(id):
    vehicle = mongo.db.vehicles.find_one_or_404({'_id': ObjectId(id)})
    response = {
        'id': str(vehicle['_id']),
        'marca': vehicle['marca'],
        'anio': vehicle['anio']
    }
    return jsonify(response)

# Ruta para crear un nuevo vehículo
@app.route('/vehicles', methods=['POST'])
def create_vehicle():
    vehicle_data = request.json
    result = mongo.db.vehicles.insert_one(vehicle_data)
    response = {'id': str(result.inserted_id)}
    return jsonify(response), 201

# Ruta para actualizar un vehículo por ID
@app.route('/vehicles/<id>', methods=['PUT'])
def update_vehicle(id):
    vehicle_data = request.json
    result = mongo.db.vehicles.update_one({'_id': ObjectId(id)}, {'$set': vehicle_data})
    if result.modified_count > 0:
        return jsonify({'message': 'Vehículo actualizado'})
    else:
        return jsonify({'message': 'Vehículo no encontrado'}), 404

# Ruta para eliminar un vehículo por ID
@app.route('/vehicles/<id>', methods=['DELETE'])
def delete_vehicle(id):
    result = mongo.db.vehicles.delete_one({'_id': ObjectId(id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'Vehículo eliminado'})
    else:
        return jsonify({'message': 'Vehículo no encontrado'}), 404

if __name__ == '__main__':
    app.run()