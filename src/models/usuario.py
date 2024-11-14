from extensions import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from werkzeug.utils import secure_filename
import os

class Vehiculo(db.Model):  # Usa db.Model, ya que Base es db.Model
    __tablename__ = 'vehiculos'

    id = Column(Integer, primary_key=True)
    matricula = Column(String(10), unique=True, nullable=False)
    propietario_id = Column(Integer, ForeignKey('propietarios.id'), nullable=False)
    marca_id = Column(Integer, ForeignKey('marcas_vehiculos.id'), nullable=False)
    modelo_id = Column(Integer, ForeignKey('modelos_vehiculos.id'), nullable=False)
    color_id = Column(Integer, ForeignKey('colores_vehiculos.id'), nullable=False)
    foto = Column(String(255))  # Almacena la ruta de la imagen
    fecha_registro = Column(DateTime, default=db.func.current_timestamp())

    # Relaciones
    propietario = relationship("Propietario", backref="vehiculos")
    marca = relationship("MarcaVehiculo", backref="vehiculos")
    modelo = relationship("ModeloVehiculo", backref="vehiculos")
    color = relationship("ColorVehiculo", backref="vehiculos")

    def __repr__(self):
        return f'<Vehiculo {self.matricula}>'

    # Método para guardar la foto de manera segura
    def save_foto(self, foto):
        if foto:
            # Asegurar el nombre de archivo
            filename = secure_filename(foto.filename)
            # Definir la ruta de almacenamiento
            foto_path = os.path.join('static', 'uploads', filename)
            # Guardar la foto en el servidor
            foto.save(foto_path)
            # Guardar la ruta de la foto en la base de datos
            self.foto = foto_path
