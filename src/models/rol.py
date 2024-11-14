from extensions import db
from models.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

class Rol(Base):
    __tablename__ = 'roles_usuarios'

    id = Column(Integer, primary_key=True)
    nombre_rol = Column(String(30), unique=True, nullable=False)

    # Relación con los usuarios
    usuarios = relationship("Usuario", backref="rol")

    def __repr__(self):
        return f'<Rol {self.nombre_rol}>'
