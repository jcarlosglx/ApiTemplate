from flask import jsonify
from flask import Response
from app.messages.errorMessages import ERROR_MSG_500
from app.messages.statusMessages import STATUS_200, STATUS_500
from app.messages.successMessages import SUCCESS_MSG_200


class MessageReturn:
    message = None
    status = None
    data = None

    def return_message(self) -> Response:
        response = jsonify(data=self.data, status=self.status, message=self.message)
        response._status = self.status
        return response

    def custom_return_message(self, data: str, message: str, status: str) -> Response:
        self.data = data
        self.status = status
        self.message = message
        return self.return_message()

    def error_id_not_found(self) -> Response:
        self.status = STATUS_500
        self.data = ""
        self.message = ERROR_MSG_500
        return self.return_message()

    def update_record_message(self, data) -> Response:
        self.status = STATUS_200
        self.data = data
        self.message = SUCCESS_MSG_200
        return self.return_message()

    def create_record_message(self, data) -> Response:
        self.status = STATUS_200
        self.data = data
        self.message = SUCCESS_MSG_200
        return self.return_message()

    def delete_record_message(self) -> Response:
        self.status = STATUS_200
        self.data = ""
        self.message = SUCCESS_MSG_200
        return self.return_message()

    def access_record_message(self, data) -> Response:
        self.status = STATUS_200
        self.data = data
        self.message = SUCCESS_MSG_200
        return self.return_message()
