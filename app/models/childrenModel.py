from sqlalchemy_serializer import SerializerMixin
from app.models import db


class ChildrenModel(db.Model, SerializerMixin):
    __tablename__ = "children_model"
    __table_args__ = {"extend_existing": True}
    serializer_rules = ()

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(50), unique=True, nullable=False)
    age: int = db.Column(db.Integer)
    parent_id: int = db.Column(db.Integer, db.ForeignKey("father_model.id"))
