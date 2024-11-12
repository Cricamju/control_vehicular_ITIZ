from flask import Blueprint, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from models.vehiculo import Vehiculo
from extensions import db
import os

vehiculos_bp = Blueprint('vehiculos', __name__)

# Definir la carpeta de imágenes y las extensiones permitidas
UPLOAD_FOLDER = os.path.join('static', 'images', 'vehiculos')
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
            # Guardar la imagen en la carpeta estática
            filename = secure_filename(foto.filename)
            foto_path = os.path.join(UPLOAD_FOLDER, filename)
            foto.save(foto_path)

            # Crear el objeto Vehiculo y guardar en la base de datos
            vehiculo = Vehiculo(
                matricula=request.form['matricula'],
                propietario_id=request.form['propietario_id'],
                marca_id=request.form['marca_id'],
                modelo_id=request.form['modelo_id'],
                color_id=request.form['color_id'],
                foto=os.path.join('static', 'images', 'vehiculos', filename)  # Guardar solo la ruta
            )
            
            db.session.add(vehiculo)
            db.session.commit()
            
            return redirect(url_for('vehiculos.vehiculo_detalle', vehiculo_id=vehiculo.id))

    return render_template('registrar_vehiculo.html')  # Formulario para registrar el vehículo

# Ruta para mostrar los detalles del vehículo
@vehiculos_bp.route('/vehiculo/<int:vehiculo_id>')
def vehiculo_detalle(vehiculo_id):
    vehiculo = Vehiculo.query.get_or_404(vehiculo_id)
    return render_template('vehiculo_detalle.html', vehiculo=vehiculo)
