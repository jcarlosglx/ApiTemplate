from app.models import db, load_models
from app.helpers.records.createRecords import create_records
from app.messages.returnMessages import MessageReturn
from flask import Response


class DatabaseController:

    def create_database(self) -> Response:
        try:
            load_models()
            db.create_all()
            create_records(10)
            return MessageReturn().create_record_message("Data")
        except Exception as error:
            db.session.rollback()
            return MessageReturn().error_id_not_found()

    def delete_database(self) -> Response:
        try:
            for table in db.metadata.tables.keys():
                db.session.execute(f"TRUNCATE TABLE {table} CASCADE")
                db.session.execute(f"ALTER SEQUENCE {table}_id_seq RESTART WITH 1")
            db.session.commit()
            return MessageReturn().create_record_message("Data")
        except Exception as error:
            db.session.rollback()
            return MessageReturn().error_id_not_found()
