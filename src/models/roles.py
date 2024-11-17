from ..extensions import db
from sqlalchemy import Column, BigInteger, String

class Rol(db.Model):
    __tablename__ = 'roles'

    id = db.Column(BigInteger, primary_key=True)
    name = db.Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f'<Rol {self.name}>'