from ..extensions import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, String, ForeignKey, DateTime
from werkzeug.utils import secure_filename
import os

class Vehiculo(db.Model):
    __tablename__ = 'vehicles'

    id = db.Column(BigInteger, primary_key=True)
    license_plate = db.Column(String(10), unique=True, nullable=False)
    owner_id = db.Column(BigInteger, ForeignKey('vehicle_owners.id'), nullable=False)
    brand_id = db.Column(BigInteger, ForeignKey('vehicle_brands.id'), nullable=False)
    color_id = db.Column(BigInteger, ForeignKey('colors.id'), nullable=False)
    photo_path = db.Column(String(255))  # Almacena la ruta de la imagen
    entry_time = db.Column(DateTime, default=db.func.current_timestamp())

    # Relaciones
    owner = relationship("PropietarioVehiculo", backref="vehiculos")
    brand = relationship("MarcaVehiculo", backref="vehiculos")
    color = relationship("ColorVehiculo", backref="vehiculos")

    def __repr__(self):
        return f'<Vehiculo {self.license_plate}>'

    # Método para guardar la foto de manera segura
    def save_foto(self, foto):
        if foto:
            # Asegurar el nombre de archivo
            filename = secure_filename(foto.filename)
            # Definir la ruta de almacenamiento
            foto_path = os.path.join('static', 'uploads', filename)
            # Guardar la foto en el servidor
            foto.save(foto_path)
            # Guardar la ruta de la foto en la base de datos
            self.photo_path = foto_path