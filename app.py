from flask import Flask
from flask_migrate import Migrate
from extensions import db, migrate  # Importar las extensiones de base de datos y migración
from routes import vehiculos_bp  # Importar el blueprint de las rutas de vehículos
from models import *  # Asegúrate de que todos los modelos sean importados

# Inicializar la aplicación Flask
app = Flask(__name__)

# Cargar la configuración desde config.py
app.config.from_object('config')  # Usa la clase Config del archivo config.py

# Inicializar las extensiones
db.init_app(app)
migrate.init_app(app, db)  # Inicializar migraciones

# Registrar el blueprint para las rutas de vehículos
app.register_blueprint(vehiculos_bp, url_prefix='/vehiculos')  # Definir un prefijo para el blueprint

# Para asegurarnos de que este archivo es el punto de entrada principal
if __name__ == '__main__':
    app.run(debug=True)  # Ejecutar la aplicación en modo debug para depuración
