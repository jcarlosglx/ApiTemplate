from flask import Response

from app.config.configDB import DBConfig
from app.helpers.records.createRecords import create_records
from app.helpers.records.deleteRecords import delete_records
from app.messages.errorMessages import (ERROR_MSG_DB_CREATED,
                                        ERROR_MSG_DB_DELETED)
from app.messages.returnMessages import MessageReturn
from app.messages.statusMessages import STATUS_200, STATUS_500
from app.messages.successMessages import (SUCCESS_MSG_DB_CREATED,
                                          SUCCESS_MSG_DB_DELETED)
from app.models.entryORM import db, load_models


class DatabaseController:
    def __init__(self):
        self.data = ""

    def create_database(self) -> Response:
        try:
            load_models()
            db.create_all()
            create_records(DBConfig.N_DUMMY_RECORDS)
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
            delete_records()
            return MessageReturn().custom_return_message(
                self.data, SUCCESS_MSG_DB_DELETED, STATUS_200
            )
        except Exception as error:
            db.session.rollback()
            return MessageReturn().custom_return_message(
                self.data, ERROR_MSG_DB_DELETED, STATUS_500
            )
