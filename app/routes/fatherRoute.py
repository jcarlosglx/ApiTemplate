from flask import Blueprint
from app.controllers.fatherController import FatherController


father_blueprint = Blueprint("father", __name__)


@father_blueprint.route("/father", methods=["POST"])
def new_father():
    return FatherController().create_record()


@father_blueprint.route("/father/<id_record>", methods=["PATCH"])
def update_father():
    return FatherController().update_record()


@father_blueprint.route("/father", methods=["GET"])
def get_fathers():
    return FatherController().get_all_records()


@father_blueprint.route("/father/<id_record>", methods=["GET"])
def get_father():
    return FatherController().get_individual_record()
