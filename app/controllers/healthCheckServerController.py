from flask import Response

from app.messages.returnMessages import MessageReturn
from app.messages.statusMessages import STATUS_200
from app.messages.successMessages import SUCCESS_HEALTH_CHECK_SERVER


class HealthCheckServerController:
    def __init__(self):
        self.data = "HealthCheckController"

    def check_server(self) -> Response:
        return MessageReturn().custom_return_message(
            self.data, SUCCESS_HEALTH_CHECK_SERVER, STATUS_200
        )
