from os import environ
from dataclasses import dataclass
from os.path import join, abspath, dirname

base_dir = abspath(dirname(__file__))
base_db = join(base_dir, "base.db")


@dataclass
class AppConfig(object):
    DEBUG: bool = True
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///" + base_db
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    APPLICATION_ROOT: str = "/api"


@dataclass
class AppDevConfig(AppConfig):
    DEBUG: bool = False
    TESTING: bool = False
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///" + base_db
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    APPLICATION_ROOT: str = "/api"


@dataclass
class AppDeployConfig(AppConfig):
    DEBUG: bool = False
    TESTING: bool = False
    if environ.get("PATH_DB"):
        SQLALCHEMY_DATABASE_URI: str = environ.get("PATH_DB")
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    APPLICATION_ROOT: str = "/api"


config_app: dict = {"DEV": AppDevConfig, "DEPLOY": AppDeployConfig}
