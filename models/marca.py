from extensions import db
from models.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

class MarcaVehiculo(Base):
    __tablename__ = 'marcas_vehiculos'

    id = Column(Integer, primary_key=True)
    nombre_marca = Column(String(50), unique=True, nullable=False)

    # Relación con vehículos
    vehiculos = relationship("Vehiculo", backref="marca")

    def __repr__(self):
        return f'<Marca {self.nombre_marca}>'
