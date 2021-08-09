from io import BytesIO
from json import loads
from typing import Dict, Iterable, NoReturn, Optional

from app.exceptions.handler import HandlerError
from app.models.entryORM import db
from app.models.logModel import LogModel


class Middleware:
    def __init__(self, app):
        self.wsgi_app = app.wsgi_app
        self.app = app
        self.redirect_msg = "You should be redirected automatically to target URL"

    def __call__(self, environ, start_response) -> Iterable:
        try:
            with self.app.test_request_context():
                is_trackable = environ["REQUEST_METHOD"] != "GET"
                if is_trackable:
                    log = self.get_commited_log()
                    self.set_request_info(log, environ)
                    self.commit()
                    response = self.wsgi_app(environ, start_response)
                    pay_load = b"".join(response).decode("utf-8")
                    json_data = self.get_json_response(pay_load)
                    self.set_response_info(log, json_data)
                    self.commit()
                    return [pay_load.encode("utf-8")]
                else:
                    return self.wsgi_app(environ, start_response)

        except Exception as error:
            with self.app.test_request_context():
                if is_trackable:
                    db.session.add(log)
                    response = HandlerError.handler_middleware_error(error)
                    self.set_response_info(log, response.json)
                    self.commit()
                else:
                    response = HandlerError.handler_middleware_error(error)
                return response(environ, start_response)

    def commit(self) -> NoReturn:
        with self.app.test_request_context():
            try:
                db.session.commit()
            except Exception as error:
                db.session.rollback()
                print("Enable to save log")

    def get_commited_log(self) -> Optional[LogModel]:
        with self.app.test_request_context():
            log = None
            try:
                log = LogModel()
            except Exception as error:
                db.session.rollback()
                print("Enable to save in database")
                print(f"Error: {error}")
            return log

    def get_json_response(self, pay_load) -> Dict:
        if self.redirect_msg not in pay_load:
            json_data = loads(pay_load)
        else:
            json_data = {"data": pay_load}
        return json_data

    def set_request_info(self, new_log, environ) -> NoReturn:
        with self.app.test_request_context():
            from werkzeug.wrappers import Request

            request_incomming = Request(environ)
            new_log.method_access = request_incomming.environ["REQUEST_METHOD"]
            keys = request_incomming.environ.keys()

            if "REQUEST_URI" in keys:
                new_log.table_db = request_incomming.environ["REQUEST_URI"]
            elif "RAW_URI" in keys:
                new_log.table_db = request_incomming.environ["RAW_URI"]

            new_log.server_name = request_incomming.environ["SERVER_NAME"]

            data_request = request_incomming.data
            new_log.incomming_data = data_request.decode("utf-8")
            request_incomming.environ["wsgi.input"] = BytesIO(data_request)
            new_log.ip_request = request_incomming.environ["REMOTE_ADDR"]
            new_log.port = request_incomming.environ.get("REMOTE_PORT")

    def set_response_info(self, new_log, json_data) -> NoReturn:
        new_log.status_code = json_data["status"]
        new_log.outcomming_data = str(json_data["data"])
