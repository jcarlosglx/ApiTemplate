from flask import Response
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import MethodNotAllowed

from app.messages.errorMessages import (ERROR_MSG_500, ERROR_MSG_DB_INTEGRITY,
                                        ERROR_MSG_METHOD_NOT_ALLOW)
from app.messages.returnMessages import MessageReturn
from app.messages.statusMessages import STATUS_405, STATUS_410, STATUS_500


class HandlerError:
    @staticmethod
    def handler_middleware_error(error: Exception) -> Response:
        message = ERROR_MSG_500
        status = STATUS_500
        data = str(error)

        if isinstance(error, IntegrityError):
            message = ERROR_MSG_DB_INTEGRITY
            status = STATUS_410

        elif isinstance(error, MethodNotAllowed):
            message = ERROR_MSG_METHOD_NOT_ALLOW
            status = STATUS_405

        response = MessageReturn().custom_return_message(data, message, status)
        response._status = status
        return response

    @staticmethod
    def handler_http_error(error: Exception) -> Response:
        message = ERROR_MSG_500
        status = STATUS_500
        data = str(error)

        if isinstance(error, IntegrityError):
            message = ERROR_MSG_DB_INTEGRITY
            status = STATUS_410

        elif isinstance(error, MethodNotAllowed):
            message = ERROR_MSG_METHOD_NOT_ALLOW
            status = STATUS_405

        response = MessageReturn().custom_return_message(data, message, status)
        response._status = status
        return response
