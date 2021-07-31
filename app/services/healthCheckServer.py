import requests
import atexit
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from app.messages.statusMessages import STATUS_200
from app.models.logModel import LogModel
from app import get_config_server
from app.config.configEndpoint import EndpointConfig
from app.models import db


class HealthCheckServer:
    def __init__(self, instance: Flask):
        config = get_config_server()
        self.ip = config.HOST
        self.port = config.PORT
        self.schedule = BackgroundScheduler(deamon=True)
        self.prefix = instance.config["APPLICATION_ROOT"]
        self.instance = instance
        self.endpoint = EndpointConfig.endpoint_health_check_server

        self.schedule.add_job(
            func=HealthCheckServer.health_check_server,
            trigger="interval",
            seconds=config.HEALTH_CHEK_SEC,
            args=[self.ip, self.port, self.instance, self.prefix, self.endpoint],
            id="deamon_server"
        )
        self.schedule.start()
        atexit.register(lambda: self.schedule.shutdown(wait=False))

    @staticmethod
    def create_log(ip: str, port: str, app: Flask, error: str):
        try:
            with app.test_request_context():
                new_log = LogModel()
                new_log.port = port
                new_log.ip_request = ip
                new_log.status_code = 500
                new_log.incomming_data = ""
                new_log.outcomming_data = f"{error}"
                new_log.method_access = "GET"
                new_log.server_name = ip
                new_log.table_db = ""
                db.session.add(new_log)
                db.session.commit()

        except Exception as error:
            db.session.rollback()
            print("Unable to save a log")
            print(f"Error: {error}")

    @staticmethod
    def health_check_server(ip: str, port: str, app: Flask, prefix: str, endpoint: str):
        try:
            with app.test_request_context():
                url_server = f"http://{ip}:{port}{prefix}{endpoint}"
                print(url_server)
                response_server = requests.get(f"{url_server}")
                data_json = response_server.json()
                if data_json["status"] != STATUS_200:
                    print(data_json["message"])
        except Exception as error:
            HealthCheckServer.create_log(ip, port, app, str(error))
