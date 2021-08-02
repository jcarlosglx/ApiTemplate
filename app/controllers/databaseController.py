from app.models.entryORM import db, load_models
from app.helpers.records.createRecords import create_records
from app.messages.returnMessages import MessageReturn
from app.messages.statusMessages import STATUS_200, STATUS_500
from app.messages.errorMessages import ERROR_MSG_DB_CREATED, ERROR_MSG_DB_DELETED
from app.messages.successMessages import SUCCESS_MSG_DB_CREATED, SUCCESS_MSG_DB_DELETED
from flask import Response


class DatabaseController:
    def __init__(self):
        self.data = str(self.__class__)

    def create_database(self) -> Response:
        try:
            load_models()
            db.create_all()
            create_records(10)
            return MessageReturn().custom_return_message(
                self.data, SUCCESS_MSG_DB_CREATED, STATUS_200
            )
        except Exception as error:
            db.session.rollback()
            return MessageReturn().custom_return_message(
                self.data, ERROR_MSG_DB_CREATED, STATUS_500
            )

    def delete_database(self) -> Response:
        try:
            for table in db.metadata.tables.keys():
                db.session.execute(f"TRUNCATE TABLE {table} CASCADE")
                db.session.execute(f"ALTER SEQUENCE {table}_id_seq RESTART WITH 1")
            db.session.commit()
            return MessageReturn().custom_return_message(
                self.data, SUCCESS_MSG_DB_DELETED, STATUS_200
            )
        except Exception as error:
            db.session.rollback()
            return MessageReturn().custom_return_message(
                self.data, ERROR_MSG_DB_DELETED, STATUS_500
            )
