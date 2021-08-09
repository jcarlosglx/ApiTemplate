from flask import Blueprint, Response

from app.config.configEndpoint import EndpointConfig
from app.controllers.databaseController import DatabaseController

database_blueprint = Blueprint("database", __name__)
endpoint_create = EndpointConfig.endpoint_database_create
endpoint_delete = EndpointConfig.endpoint_database_delete


@database_blueprint.route(f"{endpoint_create}", methods=["GET"])
def create_database() -> Response:
    return DatabaseController().create_database()


@database_blueprint.route(f"{endpoint_delete}", methods=["GET"])
def delete_database() -> Response:
    return DatabaseController().delete_database()
