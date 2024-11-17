from flask import Blueprint, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from src.models.vehicle_owners import PropietarioVehiculo  # Importar el modelo de propietario
from src.models.vehicles import Vehiculo  # Importar el modelo de vehículo
from src.models.users import Usuario  # Importar el modelo de usuario (si existe)
import os
from src.extensions import db

vehiculos_bp = Blueprint('vehiculos', __name__)

# Definir la carpeta de imágenes y las extensiones permitidas
UPLOAD_FOLDER_VEHICULOS = os.path.join('static', 'images', 'vehiculos')
UPLOAD_FOLDER_PROPIETARIOS = os.path.join('static', 'images', 'propietarios')
UPLOAD_FOLDER_USUARIOS = os.path.join('static', 'images', 'usuarios')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Función para verificar si el archivo tiene una extensión permitida
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Ruta para registrar un vehículo
@vehiculos_bp.route('/registrar_vehiculo', methods=['GET', 'POST'])
def registrar_vehiculo():
    if request.method == 'POST':
        if 'foto' not in request.files:
            return 'No file part', 400
        foto = request.files['foto']
        
        if foto.filename == '':
            return 'No selected file', 400
        
        if foto and allowed_file(foto.filename):
            # Guardar la imagen en la carpeta de vehículos
            filename = secure_filename(foto.filename)
            foto_path = os.path.join(UPLOAD_FOLDER_VEHICULOS, filename)
            foto.save(foto_path)

            # Crear el objeto Vehiculo y guardar en la base de datos
            vehiculo = Vehiculo(
                license_plate=request.form['matricula'],
                owner_id=request.form['propietario_id'],
                brand_id=request.form['marca_id'],
                color_id=request.form['color_id'],
                photo_path=os.path.join('static', 'images', 'vehiculos', filename),
            )
            
            db.session.add(vehiculo)
            db.session.commit()
            
            return redirect(url_for('vehiculos.vehiculo_detalle', vehiculo_id=vehiculo.id))

    return render_template('registrar_vehiculo.html')

# Ruta para registrar un propietario
@vehiculos_bp.route('/registrar_propietario', methods=['GET', 'POST'])
def registrar_propietario():
    if request.method == 'POST':
        if 'foto' not in request.files:
            return 'No file part', 400
        foto = request.files['foto']
        
        if foto.filename == '':
            return 'No selected file', 400
        
        if foto and allowed_file(foto.filename):
            # Guardar la imagen en la carpeta de propietarios
            filename = secure_filename(foto.filename)
            foto_path = os.path.join(UPLOAD_FOLDER_PROPIETARIOS, filename)
            foto.save(foto_path)

            # Crear el objeto PropietarioVehiculo y guardar en la base de datos
            propietario = PropietarioVehiculo(
                nombre=request.form['nombre'],
                # Otros campos que necesites
                foto_path=os.path.join('static', 'images', 'propietarios', filename),
            )
            
            db.session.add(propietario)
            db.session.commit()
            
            return redirect(url_for('vehiculos.propietario_detalle', propietario_id=propietario.id))

    return render_template('registrar_propietario.html')

# Ruta para registrar un usuario
@vehiculos_bp.route('/registrar_usuario', methods=['GET', 'POST'])
def registrar_usuario():
    if request.method == 'POST':
        if 'foto' not in request.files:
            return 'No file part', 400
        foto = request.files['foto']
        
        if foto.filename == '':
            return 'No selected file', 400
        
        if foto and allowed_file(foto.filename):
            # Guardar la imagen en la carpeta de usuarios
            filename = secure_filename(foto.filename)
            foto_path = os.path.join(UPLOAD_FOLDER_USUARIOS, filename)
            foto.save(foto_path)

            # Crear el objeto Usuario y guardar en la base de datos
            usuario = Usuario(
                nombre=request.form['nombre'],
                # Otros campos que necesites
                foto_path=os.path.join('static', 'images', 'usuarios', filename),
            )
            
            db.session.add(usuario)
            db.session.commit()
            
            return redirect(url_for('vehiculos.usuario_detalle', usuario_id=usuario.id))

    return render_template('registrar_usuario.html')