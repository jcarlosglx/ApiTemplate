from flask import Flask
from werkzeug.exceptions import default_exceptions
from app.exceptions.handler import HandlerError
from app.middleware.middleware import Middleware
from app.models import db
from app.config.configApp import config_app


def create_app(config_type: str = "DEV"):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(config_app[config_type])
    db.init_app(app)
    app.wsgi_app = Middleware(app)
    for exception in default_exceptions:
        app.register_error_handler(exception, HandlerError.handler_middleware_error)
    return app
