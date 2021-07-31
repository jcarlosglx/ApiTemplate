from flask import Blueprint
from app.controllers.childrenController import ChildrenController
from app.config.configEndpoint import ConfigurationEndpoint


children_blueprint = Blueprint("children", __name__)
endpoint = ConfigurationEndpoint.endpoint_children


@children_blueprint.route(f"{endpoint}", methods=["POST"])
def new_children():
    return ChildrenController().create_record()


@children_blueprint.route(f"{endpoint}/<id_record>", methods=["PATCH"])
def update_children(id_record):
    return ChildrenController().update_record(id_record)


@children_blueprint.route(f"{endpoint}", methods=["GET"])
def get_all_children():
    return ChildrenController().get_all_records()


@children_blueprint.route(f"{endpoint}/<id_record>", methods=["GET"])
def get_children(id_record):
    return ChildrenController().get_individual_record(id_record)
