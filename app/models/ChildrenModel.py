from app.models.baseModel import BaseModel
from app.models import db


class ChildrenModel(BaseModel):
    __tablename__ = "children_model"
    __table_args__ = {"extend_existing": True}
    serializer_rules = ()

    age = db.Column(db.Integer)
    parent_id = db.Column(db.Integer, db.ForeignKey("father_model.id"))
