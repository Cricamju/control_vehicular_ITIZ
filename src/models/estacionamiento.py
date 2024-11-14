from extensions import db
from models.base import Base
from sqlalchemy import Column, Integer, String

class Estacionamiento(Base):
    __tablename__ = 'estacionamiento'

    id = Column(Integer, primary_key=True)
    total_lugares = Column(Integer, nullable=False)
    lugares_ocupados = Column(Integer, default=0)
    ubicacion = Column(String(100), nullable=False)
    descripcion = Column(String(255))

    def __repr__(self):
        return f'<Estacionamiento {self.ubicacion}>'
