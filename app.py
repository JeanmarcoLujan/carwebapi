from flask import Flask
from flask_pymongo import PyMongo
from entities.vehicle.routes import vehicle_bp
from entities.user.routes import user_bp

app = Flask(__name__)

# Configuración de la conexión a MongoDB
app.config['MONGO_URI'] = 'mongodb+srv://jean:jean001@cluster0.dt3yttw.mongodb.net/carwash?retryWrites=true&w=majority'
mongo = PyMongo(app)

# Registrar los blueprints de las entidades
app.register_blueprint(vehicle_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run()