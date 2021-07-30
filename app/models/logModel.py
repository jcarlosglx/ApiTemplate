from app.models import db


class LogModel(db.Model):
    __tablename__ = "log_model"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    table_db = db.Column(db.String(255))
    method_access = db.Column(db.String(10))
    incomming_data = db.Column(db.Text())
    outcomming_data = db.Column(db.Text())
    server_name = db.Column(db.String(45))
    port = db.Column(db.String(10))
    ip_request = db.Column(db.String(45))
    status_code = db.Column(db.String(5))
