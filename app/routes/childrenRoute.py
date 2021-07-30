from flask import Blueprint
from app.controllers.childrenController import ChildrenController


children_blueprint = Blueprint("children", __name__)


@children_blueprint.route("/children", methods=["POST"])
def new_children():
    return ChildrenController().create_record()


@children_blueprint.route("/children/<id_record>", methods=["PATCH"])
def update_children():
    return ChildrenController().update_record()


@children_blueprint.route("/children", methods=["GET"])
def get_all_children():
    return ChildrenController().get_all_records()


@children_blueprint.route("/children/<id_record>", methods=["GET"])
def get_children():
    return ChildrenController().get_individual_record()
