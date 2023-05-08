from flask import jsonify

# Lógica para obtener todos los usuarios
def get_all_users():
    users = [
        {'id': 1, 'name': 'John Doe'},
        {'id': 2, 'name': 'Jane Smith'}
    ]
    return jsonify(users)

# Lógica para obtener un usuario por ID
def get_user_by_id(user_id):
    user = {'id': user_id, 'name': 'John Doe'}
    return jsonify(user)