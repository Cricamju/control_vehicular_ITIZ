from ..extensions import db
from sqlalchemy import Column, BigInteger, String, Boolean

class EspacioEstacionamiento(db.Model):
    __tablename__ = 'parking_spots'

    id = db.Column(BigInteger, primary_key=True)
    spot_number = db.Column(String, unique=True, nullable=False)
    is_occupied = db.Column(Boolean, default=False)

    def __repr__(self):
        return f'<Espacio {self.spot_number}>'