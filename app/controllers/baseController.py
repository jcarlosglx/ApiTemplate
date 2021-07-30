from flask import request
from app.models import db
from app.exceptions.handler import HandlerError
from app.messages.returnMessages import MessageReturn
from sqlalchemy.exc import SQLAlchemyError


class BaseController:
    model = None
    data_json = request.get_json()
    schema = None
    rules = None

    def update_record(self, id_record):
        self.data_json = request.get_json()
        result = self.model.query.filter_by(id=id_record)
        if not result:
            return MessageReturn().error_id_not_found()
        schema = self.schema()
        schema.load(self.data_json, partial=True)
        result.update(self.data_json)
        try:
            db.session.commit()
        except SQLAlchemyError as error:
            db.session.rollback()
            return HandlerError.handler_middleware_error(error)
        data = result.first().to_dict()
        return MessageReturn().update_record_message(data)

    def get_individual_record(self, id_record):
        self.data_json = request.get_json()
        result = self.model.query.filter_by(id=id_record).first()
        if not result:
            return MessageReturn().error_id_not_found()

        if self.rules:
            data = result.to_dict(rules=self.rules)
        else:
            data = result.to_dict()
        return MessageReturn().access_record_message(data)

    def get_all_records(self):
        self.data_json = request.get_json()
        results = self.model.query.all()
        if not results:
            return MessageReturn().error_id_not_found()

        if self.rules:
            data = [result.to_dict(rules=self.rules) for result in results]
        else:
            data = [result.to_dict() for result in results]
        return MessageReturn().access_record_message(data)

    def create_record(self):
        self.data_json = request.get_json()
        schema = self.schema()
        valid_data = schema.load(self.data_json)
        new_record = self.model(**valid_data)
        try:
            db.session.add(new_record)
            db.session.commit()
        except SQLAlchemyError as error:
            db.session.rollback()
            return HandlerError.handler_middleware_error(error)

        data = new_record.first().to_dict()
        return MessageReturn().create_record_message(data)

    def delete_record(self, id_record):
        self.data_json = request.get_json()
        result = self.model.query.filter_by(id=id_record).first()
        if not result:
            return MessageReturn().error_id_not_found()
        try:
            db.session.delete(result)
            db.session.commit()
        except SQLAlchemyError as error:
            db.session.rollback()
            return HandlerError.handler_middleware_error(error)

        return MessageReturn().delete_record_message()
