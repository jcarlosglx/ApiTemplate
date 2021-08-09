from os import environ

from flask import Flask
from werkzeug.exceptions import default_exceptions

from app.config.configApp import AppConfig, config_app
from app.config.configDB import DBConfig, config_db
from app.config.configServer import ServerConfig, config_server
from app.exceptions.handler import HandlerError
from app.middleware.middleware import Middleware
from app.models.entryORM import db


def create_app() -> Flask:
    app = Flask(__name__)
    config = get_config_app()
    app.config.from_object(config)
    db.init_app(app)
    app.wsgi_app = Middleware(app)
    for exception in default_exceptions:
        app.register_error_handler(exception, HandlerError.handler_http_error)
    return app


def check_connection_db() -> bool:
    try:
        db.session.execute("SELECT 1")
        return True
    except Exception as error:
        return False


def get_config_app(type_config: str = "") -> AppConfig:
    if type_config != "":
        return config_app[type_config]
    type_configuration = "DEV"
    if environ.get("PATH_DB"):
        type_configuration = "DEPLOY"
    return config_app[type_configuration]


def get_config_db(type_config: str = "") -> DBConfig:
    if type_config != "":
        return config_db[type_config]
    type_configuration = "DEV"
    if environ.get("PATH_DB"):
        type_configuration = "DEPLOY"
    return config_db[type_configuration]


def get_config_server(type_config: str = "") -> ServerConfig:
    if type_config != "":
        return config_server[type_config]
    type_configuration = "DEV"
    if environ.get("NAME_SERVER_API") and environ.get("PORT_SERVER_API"):
        type_configuration = "DEPLOY"
    return config_server[type_configuration]
