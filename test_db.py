from src.app import create_app
from src.extensions import db
from src.models.vehicle_owners import PropietarioVehiculo
from src.models.vehicles import Vehiculo
# Importa otros modelos si es necesario

app = create_app()

with app.app_context():
    try:
        # Intenta crear todas las tablas definidas en los modelos
        db.create_all()
        print("Conexión a la base de datos exitosa y tablas creadas (si no existían).")
    except Exception as e:
        print("Error al conectar a la base de datos:", e)