"""
docsting for app module
"""
# coding: utf-8
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

db = SQLAlchemy()

def create_app(config_name="dev"):
    """
    docsting for create_app method
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    Bootstrap(app)
    db.init_app(app)

    Migrate(app, db)

    from .spiders import spiders as spider_app

    app.register_blueprint(spider_app)

    logging.basicConfig()

    return app
