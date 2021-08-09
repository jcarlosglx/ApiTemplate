from app.entryApp import create_app, check_connection_db
from app.routes.blueprints import load_blueprints
from flask import Flask
import pytest
from typing import Type
from flask_sqlalchemy import SQLAlchemy
from app.models.entryORM import load_models, CustomSQLAlchemy


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
            db = CustomSQLAlchemy
            yield db
        else:
            print("Unable to connect with teh dabase")