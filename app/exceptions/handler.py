from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import MethodNotAllowed
from app.messages.returnMessages import MessageReturn


class HandlerError:
    @staticmethod
    def handler_middleware_error(error: Exception):
        data = ""
        message = "Error Server"
        status = 500

        if isinstance(error, IntegrityError):
            data = str(error.__class__)
            message = "Error: Data not acceptable"
            status = 500
        elif isinstance(error, MethodNotAllowed):
            data = str(error.__class__)
            message = "Error: Not able to access"
            status = 500

        response = MessageReturn().custom_return_message(data, message, status)
        response._status = status
        return response
