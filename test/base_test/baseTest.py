from requests import get, post, patch, delete, put
from typing import Type
from marshmallow import Schema
from app.messages.statusMessages import STATUS_200
from test.helpers.dummy_json_test.dummy_json_test import get_dummy_json_test
from test.config.configTest import ConfigTest
from app.entryApp import create_app, check_connection_db
from app.routes.blueprints import load_blueprints
from app.models.entryORM import load_models, CustomSQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from typing import Type
from flask import Flask
import pytest


class BaseGetTest:
    expect_status_get: str = STATUS_200
    url_get: str = ConfigTest.URL
    endpoint_get: str
    response_key: str = ConfigTest.response_key

    @pytest.fixture
    def get_app(self) -> Flask:
        app = create_app()
        yield app

    @pytest.fixture
    def get_db(self, get_app: Flask) -> Type[SQLAlchemy]:
        load_models()
        with get_app.test_request_context():
            load_blueprints(get_app)
            is_alive_db = check_connection_db()
            if is_alive_db:
                db = CustomSQLAlchemy
                yield db
            else:
                print("Unable to connect with teh dabase")

    def test_get(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        response = get_app.test_client().get(f"{self.url_get}{self.endpoint_get}")
        code_response = response.get_json()[self.response_key]
        assert code_response == self.expect_status_get, f"Expected {self.expect_status_get} got {code_response}"


class BaseDeleteTest:
    id_delete: int = 2
    expect_status_delete: str = STATUS_200
    url_delete: str = ConfigTest.URL
    endpoint_delete: str
    response_key: str = ConfigTest.response_key

    def test_delete(self):
        response = delete(f"{self.url_delete}{self.endpoint_delete}/{self.id_delete}")
        assert response.json()[self.response_key] == self.expect_status_delete


class BasePostTest:
    expect_status_post: str = STATUS_200
    url_post: str = ConfigTest.URL
    endpoint_post: str
    response_key: str = ConfigTest.response_key
    schema_post: Type[Schema]

    def test_post(self):
        json_data = get_dummy_json_test(self.schema_post)
        response = post(f"{self.url_post}{self.endpoint_post}", json=json_data)
        assert response.json()[self.response_key] == self.expect_status_post


class BasePatchTest:
    id_patch: int = 3
    expect_status_patch: str = STATUS_200
    url_patch: str = ConfigTest.URL
    endpoint_patch: str
    response_key: str = ConfigTest.response_key
    schema_patch: Type[Schema]

    def test_patch(self):
        json_data = get_dummy_json_test(self.schema_patch)
        response = patch(
            f"{self.url_patch}{self.endpoint_patch}/{self.id_patch}", json=json_data
        )
        assert response.json()[self.response_key] == self.expect_status_patch


class BasePutTest:
    id_put: int = 3
    expect_status_put: str = STATUS_200
    url_put: str = ConfigTest.URL
    endpoint_put: str
    response_key: str = ConfigTest.response_key
    schema_put: Type[Schema]

    def test_patch(self):
        json_data = get_dummy_json_test(self.schema_put)
        response = put(
            f"{self.url_put}{self.endpoint_put}/{self.id_put}", json=json_data
        )
        assert response.json()[self.response_key] == self.expect_status_put
