from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Inicializar las extensiones
db = SQLAlchemy()
migrate = Migrate()
