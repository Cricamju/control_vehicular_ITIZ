from ..extensions import db
from sqlalchemy import Column, BigInteger, String

class MarcaVehiculo(db.Model):
    __tablename__ = 'vehicle_brands'

    id = db.Column(BigInteger, primary_key=True)
    name = db.Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f'<Marca {self.name}>'