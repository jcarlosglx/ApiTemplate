from app.messages.returnMessages import MessageReturn
from app.messages.statusMessages import STATUS_200
from flask import Response


class HealthCheckServerController:
    def check_server(self) -> Response:
        return MessageReturn().custom_return_message("", "Ok server", STATUS_200)
