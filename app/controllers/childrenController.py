from app.controllers.baseController import BaseController
from app.models.childrenModel import ChildrenModel
from app.schemas.childrenSchema import ChildrenSchema


class ChildrenController(BaseController):
    model = ChildrenModel
    schema = ChildrenSchema
    rules = ChildrenModel.serialize_rules
