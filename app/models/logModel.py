from app.models.entryORM import db


class LogModel(db.Model):
    __tablename__ = "log_model"
    __table_args__ = {"extend_existing": True}

    id: int = db.Column(db.Integer, primary_key=True)
    table_db: str = db.Column(db.String(255))
    method_access: str = db.Column(db.String(10))
    incomming_data: str = db.Column(db.Text())
    outcomming_data: str = db.Column(db.Text())
    server_name: str = db.Column(db.String(45))
    port: str = db.Column(db.String(10))
    ip_request: str = db.Column(db.String(45))
    status_code: str = db.Column(db.String(5))
