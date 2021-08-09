from flask import Blueprint, Response

from app.config.configEndpoint import EndpointConfig
from app.controllers.fatherController import FatherController

father_blueprint = Blueprint("father", __name__)
endpoint = EndpointConfig.endpoint_father


@father_blueprint.route(f"{endpoint}", methods=["POST"])
def new_father() -> Response:
    return FatherController().create_record()


@father_blueprint.route(f"{endpoint}/<id_record>", methods=["PATCH"])
def update_father(id_record) -> Response:
    return FatherController().update_record(id_record)


@father_blueprint.route(f"{endpoint}/<id_record>", methods=["DELETE"])
def delete_father(id_record) -> Response:
    return FatherController().delete_record(id_record)


@father_blueprint.route(f"{endpoint}", methods=["GET"])
def get_fathers() -> Response:
    return FatherController().get_all_records()


@father_blueprint.route(f"{endpoint}/<id_record>", methods=["GET"])
def get_father(id_record) -> Response:
    return FatherController().get_individual_record(id_record)
