from flask import Flask
from flask_migrate import Migrate
from flask.cli import FlaskGroup
from src.app import create_app
from src.extensions import db

app = create_app()
migrate = Migrate(app, db)

cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()