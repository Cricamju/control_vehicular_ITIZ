from extensions import db, migrate
from routes import vehiculos_bp
from flask import Flask
from flask_migrate import Migrate
from models import * # Asegúrate de que todos los modelos sean importados

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:0426@localhost:5432/control_vehicular'
    # Cargar la configuración desde config.py
    app.config.from_object('config.Config')  # Asumiendo que la clase Config está en config.py

    # Inicializar las extensiones con la app
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar el blueprint para las rutas de vehículos
    app.register_blueprint(vehiculos_bp, url_prefix='/vehiculos')

    return app