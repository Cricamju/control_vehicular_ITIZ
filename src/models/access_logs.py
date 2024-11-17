from ..extensions import db
from sqlalchemy import Column, BigInteger, DateTime, ForeignKey

class RegistroAcceso(db.Model):
    __tablename__ = 'access_logs'

    id = db.Column(BigInteger, primary_key=True)
    vehicle_id = db.Column(BigInteger, ForeignKey('vehicles.id'), nullable=False)
    entry_time = db.Column(DateTime, default=db.func.current_timestamp())
    exit_time = db.Column(DateTime)

    def __repr__(self):
        return f'<RegistroAcceso {self.id}, Vehículo ID: {self.vehicle_id}>'