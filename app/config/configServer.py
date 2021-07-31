from dataclasses import dataclass
from os import environ


@dataclass
class ServerConfig:
    HOST = "0.0.0.0"
    PORT = 8080
    TIME_WAKE_SEC = 8
    HEALTH_CHEK_SEC = 10
    DEBUG = True


@dataclass
class ServerDevConfig(ServerConfig):
    HOST = "0.0.0.0"
    PORT = 8080
    DEBUG = True


@dataclass
class ServerDeployConfig(ServerConfig):
    if environ.get("NAME_SERVER_API"):
        HOST = environ.get("NAME_SERVER_API")
    if environ.get("PORT_SERVER_API"):
        PORT = environ.get("PORT_SERVER_API")
    DEBUG = False


config_server = {
    "DEV": ServerDevConfig,
    "DEPLOY": ServerDeployConfig
}
