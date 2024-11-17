from flask import Flask
from src.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Cargar la configuración desde config.py

    # Inicializar las extensiones con la app
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar el blueprint para las rutas de vehículos
    from src.routes import vehiculos_bp
    app.register_blueprint(vehiculos_bp)

    return app