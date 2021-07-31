from os import environ
from dataclasses import dataclass
from os.path import join, abspath, dirname

base_dir = abspath(dirname(__file__))
base_db = join(base_dir, "base.db")


@dataclass
class AppConfig(object):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + base_db
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APPLICATION_ROOT = "/api"


@dataclass
class DevConfig(AppConfig):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + base_db
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APPLICATION_ROOT = "/api"


@dataclass
class DeployConfig(AppConfig):
    DEBUG = False
    TESTING = False
    if environ.get("PATH_DB"):
        SQLALCHEMY_DATABASE_URI = environ.get("PATH_DB")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APPLICATION_ROOT = "/api"


config_app = {
    "DEV": DevConfig,
    "DEPLOY": DeployConfig
}
