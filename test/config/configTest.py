from dataclasses import dataclass
from app.config.configEndpoint import EndpointConfig
from app.config.configServer import ServerDevConfig
from app.config.configApp import AppDevConfig


@dataclass
class ConfigTest(EndpointConfig, ServerDevConfig, AppDevConfig):
    HOST: str = ServerDevConfig.HOST
    PORT: int = ServerDevConfig.PORT
    PREFIX: str = AppDevConfig.APPLICATION_ROOT
    URL: str = f"http://{HOST}:{PORT}{PREFIX}"
    response_key: str = "status"
