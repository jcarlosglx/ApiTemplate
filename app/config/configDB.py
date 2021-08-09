from dataclasses import dataclass
from os import environ
from os.path import abspath, dirname, join

base_dir = abspath(dirname(__file__))
base_db = join(base_dir, "devDB.db")


@dataclass
class DBConfig(object):
    PATH: str = "sqlite:///" + base_db
    N_DUMMY_RECORDS: int = 10


@dataclass
class DBDevConfig(DBConfig):
    pass


@dataclass
class DBDeployConfig(DBConfig):
    if environ.get("PATH_DB"):
        PATH: str = environ.get("PATH_DB")


config_db: dict = {"DEV": DBDevConfig, "DEPLOY": DBDeployConfig}
