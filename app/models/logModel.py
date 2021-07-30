from app.models.baseModel import BaseModel
from app.models import db


class LogModel(BaseModel):
    __tablename__ = "log_model"
    __table_args__ = {"extend_existing": True}
    serializer_rules = ()

    table_db = db.Column(db.String(255))
    method_access = db.Column(db.String(10))
    incomming_data = db.Column(db.Text())
    outcomming_data = db.Column(db.Text())
    server_name = db.Column(db.String(45))
    port = db.Column(db.String(10))
    ip_request = db.Column(db.String(45))
    status_code = db.Column(db.String(5))
