from ..extensions import db
from sqlalchemy import Column, BigInteger, String

class PropietarioVehiculo(db.Model):
    __tablename__ = 'vehicle_owners'

    id = db.Column(BigInteger, primary_key=True)
    name = db.Column(String, nullable=False)
    contact_info = db.Column(String)

    def __repr__(self):
        return f'<Propietario {self.name}>'