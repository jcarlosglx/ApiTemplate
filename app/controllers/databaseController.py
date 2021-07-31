from app.models import db, load_models
from app.helpers.records.createRecords import create_records
from app.messages.returnMessages import MessageReturn
from app.messages.statusMessages import STATUS_200, STATUS_500
from app.messages.errorMessages import ERROR_MSG_500
from app.messages.successMessages import SUCCESS_MSG_200
from flask import Response


class DatabaseController:
    def create_database(self) -> Response:
        try:
            load_models()
            db.create_all()
            create_records(10)
            return MessageReturn().custom_return_message(
                "", "Database created", STATUS_200
            )
        except Exception as error:
            db.session.rollback()
            return MessageReturn().custom_return_message(
                "", "Error: Unable to create database", STATUS_500
            )

    def delete_database(self) -> Response:
        try:
            for table in db.metadata.tables.keys():
                db.session.execute(f"TRUNCATE TABLE {table} CASCADE")
                db.session.execute(f"ALTER SEQUENCE {table}_id_seq RESTART WITH 1")
            db.session.commit()
            return MessageReturn().custom_return_message(
                "", "Database deleted", STATUS_200
            )
        except Exception as error:
            db.session.rollback()
            return MessageReturn().custom_return_message(
                "", "Error: Unable to delete database", STATUS_500
            )
