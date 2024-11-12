from extensions import db
from models.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

class Propietario(Base):
    __tablename__ = 'propietarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    telefono = Column(String(15), nullable=False)
    email = Column(String(100), unique=True)

    # Relación con los vehículos
    vehiculos = relationship("Vehiculo", backref="propietario")

    def __repr__(self):
        return f'<Propietario {self.nombre} {self.apellido}>'
