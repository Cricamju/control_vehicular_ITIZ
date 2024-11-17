from ..extensions import db
from sqlalchemy import Column, BigInteger, String

class ColorVehiculo(db.Model):
    __tablename__ = 'colors'

    id = db.Column(BigInteger, primary_key=True)
    name = db.Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f'<Color {self.name}>'