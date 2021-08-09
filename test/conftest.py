from typing import Type

import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.entryApp import check_connection_db, create_app
from app.models.entryORM import CustomSQLAlchemy, load_models
from app.routes.blueprints import load_blueprints


@pytest.fixture(scope="session")
def get_app() -> Flask:
    app = create_app()
    yield app


@pytest.fixture(scope="session")
def get_db(get_app: Flask) -> Type[SQLAlchemy]:
    load_models()
    with get_app.test_request_context():
        load_blueprints(get_app)
        is_alive_db = check_connection_db()
        if is_alive_db:
            db = CustomSQLAlchemy()
            yield db
        else:
            print("Unable to connect with teh dabase")
