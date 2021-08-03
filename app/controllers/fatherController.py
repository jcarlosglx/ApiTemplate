from app.controllers.baseController import BaseController
from app.models.fatherModel import FatherModel
from app.schemas.fatherSchema import FatherSchema


class FatherController(BaseController):
    model = FatherModel
    schema = FatherSchema
    rules = FatherModel.serialize_rules
