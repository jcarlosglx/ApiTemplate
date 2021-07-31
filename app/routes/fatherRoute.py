from flask import Blueprint
from app.controllers.fatherController import FatherController
from app.config.configEndpoint import ConfigurationEndpoint


father_blueprint = Blueprint("father", __name__)
endpoint = ConfigurationEndpoint.endpoint_father


@father_blueprint.route(f"{endpoint}", methods=["POST"])
def new_father():
    return FatherController().create_record()


@father_blueprint.route(f"{endpoint}/<id_record>", methods=["PATCH"])
def update_father(id_record):
    return FatherController().update_record(id_record)


@father_blueprint.route(f"{endpoint}", methods=["GET"])
def get_fathers():
    return FatherController().get_all_records()


@father_blueprint.route(f"{endpoint}/<id_record>", methods=["GET"])
def get_father(id_record):
    return FatherController().get_individual_record(id_record)
