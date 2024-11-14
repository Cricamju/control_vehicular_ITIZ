from flask_sqlalchemy import SQLAlchemy
from extensions import db
Base = db.Model  # Esto permite a todos los modelos heredar de db.Model
