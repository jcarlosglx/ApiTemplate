from dataclasses import dataclass

from app.config.configDB import DBConfig, DBDeployConfig, DBDevConfig


@dataclass
class AppConfig(object):
    DEBUG: bool = True
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI: str = DBConfig.PATH
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    APPLICATION_ROOT: str = "/api"


@dataclass
class AppDevConfig(AppConfig):
    DEBUG: bool = False
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI: str = DBDevConfig.PATH


@dataclass
class AppDeployConfig(AppConfig):
    DEBUG: bool = False
    TESTING: bool = False
    SQLALCHEMY_DATABASE_URI: str = DBDeployConfig.PATH


config_app: dict = {"DEV": AppDevConfig, "DEPLOY": AppDeployConfig}
