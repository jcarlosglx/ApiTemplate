from typing import Dict, List

from flask import Response, request
from sqlalchemy.exc import SQLAlchemyError

from app.exceptions.handler import HandlerError
from app.messages.returnMessages import MessageReturn
from app.models.entryORM import db


class BaseController:
    model = None
    data_json = request.get_json()
    schema = None
    rules = None

    def commit_change(self) -> bool:
        try:
            db.session.commit()
            return True
        except SQLAlchemyError as error:
            db.session.rollback()
            return False

    def get_flat_data(self, results) -> List[Dict]:
        return [result.to_dict(rules=self.rules) for result in results]

    def update_record(self, id_record) -> Response:
        self.data_json = request.get_json()
        result = self.model.query.filter_by(id=id_record)
        if not result:
            return MessageReturn().error_id_not_found()
        schema = self.schema()
        schema.load(self.data_json, partial=True)
        result.update(self.data_json)
        if not self.commit_change():
            return HandlerError.handler_middleware_error(SQLAlchemyError())
        data = result.first().to_dict(rules=self.rules)
        return MessageReturn().update_record_message(data)

    def get_individual_record(self, id_record) -> Response:
        self.data_json = request.get_json()
        result = self.model.query.filter_by(id=id_record).first()
        if not result:
            return MessageReturn().error_id_not_found()
        data = result.to_dict(rules=self.rules)
        return MessageReturn().access_record_message(data)

    def get_all_records(self) -> Response:
        self.data_json = request.get_json()
        results = self.model.query.all()
        if not results:
            return MessageReturn().error_id_not_found()
        data = self.get_flat_data(results)
        return MessageReturn().access_record_message(data)

    def create_record(self) -> Response:
        self.data_json = request.get_json()
        schema = self.schema()
        valid_data = schema.load(self.data_json)
        new_record = self.model(**valid_data)
        db.session.add(new_record)
        if not self.commit_change():
            return HandlerError.handler_middleware_error(SQLAlchemyError())

        data = new_record.to_dict(rules=self.rules)
        return MessageReturn().create_record_message(data)

    def delete_record(self, id_record) -> Response:
        result = self.model.query.filter_by(id=id_record).first()
        if not result:
            return MessageReturn().error_id_not_found()
        db.session.delete(result)
        if not self.commit_change():
            return HandlerError.handler_middleware_error(SQLAlchemyError())
        return MessageReturn().delete_record_message()
