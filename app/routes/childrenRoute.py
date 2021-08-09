from flask import Blueprint, Response

from app.config.configEndpoint import EndpointConfig
from app.controllers.childrenController import ChildrenController

children_blueprint = Blueprint("children", __name__)
endpoint = EndpointConfig.endpoint_children


@children_blueprint.route(f"{endpoint}", methods=["POST"])
def new_children() -> Response:
    return ChildrenController().create_record()


@children_blueprint.route(f"{endpoint}/<id_record>", methods=["PATCH"])
def update_children(id_record) -> Response:
    return ChildrenController().update_record(id_record)


@children_blueprint.route(f"{endpoint}/<id_record>", methods=["DELETE"])
def delete_children(id_record) -> Response:
    return ChildrenController().delete_record(id_record)


@children_blueprint.route(f"{endpoint}", methods=["GET"])
def get_all_children() -> Response:
    return ChildrenController().get_all_records()


@children_blueprint.route(f"{endpoint}/<id_record>", methods=["GET"])
def get_children(id_record) -> Response:
    return ChildrenController().get_individual_record(id_record)
