from flask import Flask
from extensions import db, migrate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask.cli import FlaskGroup
from src.app import create_app

app = create_app()
migrate = Migrate(app, db)

cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()
