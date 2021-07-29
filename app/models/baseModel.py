from datetime import datetime
from sqlalchemy_serializer import SerializerMixin
from app.models import db


class BaseModel(db.Model, SerializerMixin):
    __tablename__ = "base_model"
    __table_args__ = {"extend_existing": True}
    serializer_rules = ()

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    date_creation = db.Column(db.DateTime, default=datetime.now)
    date_modification = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)