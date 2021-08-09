from flask import Blueprint, Response

from app.config.configEndpoint import EndpointConfig
from app.controllers.healthCheckServerController import \
    HealthCheckServerController

health_check_server_blueprint = Blueprint("health_check_server", __name__)
endpoint = EndpointConfig.endpoint_health_check_server


@health_check_server_blueprint.route(f"{endpoint}", methods=["GET"])
def check_server() -> Response:
    return HealthCheckServerController().check_server()
