from dataclasses import dataclass
from os import environ


@dataclass
class ServerConfig:
    HOST: str = "0.0.0.0"
    PORT: int = 8080
    TIME_WAKE_SEC: int = 8
    HEALTH_CHEK_SEC: int = 120
    DEBUG: bool = True


@dataclass
class ServerDevConfig(ServerConfig):
    HOST: str = "0.0.0.0"
    PORT: int = 8080
    DEBUG: bool = False


@dataclass
class ServerDeployConfig(ServerConfig):
    if environ.get("NAME_SERVER_API"):
        HOST: str = environ.get("NAME_SERVER_API")
    if environ.get("PORT_SERVER_API"):
        PORT: int = int(environ.get("PORT_SERVER_API"))
    DEBUG = False


config_server: dict = {"DEV": ServerDevConfig, "DEPLOY": ServerDeployConfig}
