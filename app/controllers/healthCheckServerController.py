from app.messages.returnMessages import MessageReturn
from flask import Response


class HealthCheckServerController:
    def check_server(self) -> Response:
        return MessageReturn().access_record_message("")
