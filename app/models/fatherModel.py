from sqlalchemy_serializer import SerializerMixin

from app.models.entryORM import db


class FatherModel(db.Model, SerializerMixin):
    __tablename__ = "father_model"
    __table_args__ = {"extend_existing": True}
    serialize_rules = ("-children.father",)

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(50), unique=True, nullable=False)
    age: int = db.Column(db.Integer)
    children = db.relationship(
        "ChildrenModel", back_populates="father", cascade="all, delete-orphan"
    )
