from extensions import db
from models.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

class ColorVehiculo(Base):
    __tablename__ = 'colores_vehiculos'

    id = Column(Integer, primary_key=True)
    nombre_color = Column(String(30), unique=True, nullable=False)

    # Relación con vehículos
    vehiculos = relationship("Vehiculo", backref="color")

    def __repr__(self):
        return f'<Color {self.nombre_color}>'
