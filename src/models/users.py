from ..extensions import db
from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship

class Usuario(db.Model):
    __tablename__ = 'users'

    id = db.Column(BigInteger, primary_key=True)
    username = db.Column(String, unique=True, nullable=False)
    email = db.Column(String, unique=True, nullable=False)
    password = db.Column(String, nullable=False)
    role_id = db.Column(BigInteger, ForeignKey('roles.id'), nullable=False)
    name = db.Column(String)
    photo_path = db.Column(String)

    # Relación con roles
    role = relationship("Rol", backref="usuarios")

    def __repr__(self):
        return f'<Usuario {self.username}>'