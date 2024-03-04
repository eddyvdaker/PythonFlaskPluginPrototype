from flask.cli import FlaskGroup

from src.app import create_app

cli = FlaskGroup(create_app=create_app)
