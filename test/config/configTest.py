from dataclasses import dataclass
from app.config.configEndpoint import EndpointConfig
from app.config.configServer import ServerDevConfig
from app.config.configApp import AppDevConfig


@dataclass
class ConfigTest(EndpointConfig, ServerDevConfig, AppDevConfig):
    URL: str = f"{ServerDevConfig.HOST}:{ServerDevConfig.PORT}{AppDevConfig.SQLALCHEMY_DATABASE_URI}"
