from extensions import db
from models.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

class ModeloVehiculo(Base):
    __tablename__ = 'modelos_vehiculos'

    id = Column(Integer, primary_key=True)
    nombre_modelo = Column(String(50), unique=True, nullable=False)

    # Relación con vehículos
    vehiculos = relationship("Vehiculo", backref="modelo")

    def __repr__(self):
        return f'<Modelo {self.nombre_modelo}>'
