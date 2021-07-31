from flask import Blueprint
from app.controllers.healthCheckServerController import HealthCheckServerController
from app.config.configEndpoint import EndpointConfig


health_check_server_blueprint = Blueprint("health_check_server", __name__)
endpoint = EndpointConfig.endpoint_health_check_server


@health_check_server_blueprint.route(f"{endpoint}", methods=["GET"])
def get_all_children():
    return HealthCheckServerController().check_server()
