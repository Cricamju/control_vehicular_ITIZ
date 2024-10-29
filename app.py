from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgrees:123456@localhost/postgres?client_encoding=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Usuarios(db.Model):
    __tablename__ = 'usuarios'  # Cambiado a 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    contrasena = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(50), nullable=False)

class Vehiculos(db.Model):
    __tablename__ = 'vehiculos'
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(10), unique=True, nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    propietario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

class Entradas(db.Model):
    __tablename__ = 'entradas'
    id = db.Column(db.Integer, primary_key=True)
    vehiculo_id = db.Column(db.Integer, db.ForeignKey('vehiculos.id'), nullable=False)
    fecha_hora_entrada = db.Column(db.DateTime, nullable=False)

class Salidas(db.Model):
    __tablename__ = 'salidas'
    id = db.Column(db.Integer, primary_key=True)
    vehiculo_id = db.Column(db.Integer, db.ForeignKey('vehiculos.id'), nullable=False)
    fecha_hora_salida = db.Column(db.DateTime, nullable=False)

@app.route('/add_user')
def add_user():
    nuevo_usuario = Usuarios(nombre='Juan', correo='juan@example.com', contrasena='1234', rol='admin')
    db.session.add(nuevo_usuario)
    db.session.commit()
    return 'Usuario agregado!'

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Solo se llama aquí
    app.run(debug=True)
