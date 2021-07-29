from app.models.baseModel import BaseModel
from app.models import db


class FatherModel(BaseModel):
    __tablename__ = "father_model"
    __table_args__ = {"extend_existing": True}
    serializer_rules = ()

    age = db.Column(db.Integer)
    children = db.relationship("ChildrenModel", cascade="all, delete-orphan")