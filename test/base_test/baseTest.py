from test.config.configTest import ConfigTest
from test.helpers.dummy_json_test.dummy_json_test import get_dummy_json_test
from typing import Type

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema

from app.messages.statusMessages import STATUS_200


class BaseGetIndividualTest:
    expect_status_get: str = STATUS_200
    url_get: str = ConfigTest.URL
    endpoint_get: str
    id_get: int = 1
    response_key: str = ConfigTest.response_key

    def test_get_individual(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        response = get_app.test_client().get(
            f"{self.url_get}{self.endpoint_get}/{self.id_get}"
        )
        code_response = response.get_json()[self.response_key]
        assert (
            code_response == self.expect_status_get
        ), f"Expected {self.expect_status_get} got {code_response}"


class BaseGetGeneralTest:
    expect_status_get: str = STATUS_200
    url_get: str = ConfigTest.URL
    endpoint_get: str
    response_key: str = ConfigTest.response_key

    def test_get_general(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        response = get_app.test_client().get(f"{self.url_get}{self.endpoint_get}")
        code_response = response.get_json()[self.response_key]
        assert (
            code_response == self.expect_status_get
        ), f"Expected {self.expect_status_get} got {code_response}"


class BaseDeleteTest:
    id_delete: int = 2
    expect_status_delete: str = STATUS_200
    url_delete: str = ConfigTest.URL
    endpoint_delete: str
    response_key: str = ConfigTest.response_key

    def test_delete(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        response = get_app.test_client().delete(
            f"{self.url_delete}{self.endpoint_delete}/{self.id_delete}"
        )
        code_response = response.get_json()[self.response_key]
        print(response.get_json())
        assert (
            code_response == self.expect_status_delete
        ), f"Expected {self.expect_status_delete} got {code_response}"


class BasePostTest:
    expect_status_post: str = STATUS_200
    url_post: str = ConfigTest.URL
    endpoint_post: str
    response_key: str = ConfigTest.response_key
    schema_post: Type[Schema]

    def test_post(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = get_dummy_json_test(self.schema_post)
        print(json_data)
        response = get_app.test_client().post(
            f"{self.url_post}{self.endpoint_post}",
            json=json_data,
            follow_redirects=True,
        )
        code_response = response.get_json()[self.response_key]
        print(response.get_json())
        assert (
            code_response == self.expect_status_post
        ), f"Expected {self.expect_status_post} got {code_response}"


class BasePatchTest:
    id_patch: int = 3
    expect_status_patch: str = STATUS_200
    url_patch: str = ConfigTest.URL
    endpoint_patch: str
    response_key: str = ConfigTest.response_key
    schema_patch: Type[Schema]

    def test_patch(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = get_dummy_json_test(self.schema_patch)
        response = get_app.test_client().patch(
            f"{self.url_patch}{self.endpoint_patch}/{self.id_patch}", json=json_data
        )
        code_response = response.get_json()[self.response_key]
        assert (
            code_response == self.expect_status_patch
        ), f"Expected {self.expect_status_patch} got {code_response}"


class BasePutTest:
    id_put: int = 3
    expect_status_put: str = STATUS_200
    url_put: str = ConfigTest.URL
    endpoint_put: str
    response_key: str = ConfigTest.response_key
    schema_put: Type[Schema]

    def test_put(self, get_app: Flask, get_db: Type[SQLAlchemy]):
        json_data = get_dummy_json_test(self.schema_put)
        response = get_app.test_client().put(
            f"{self.url_put}{self.endpoint_put}/{self.id_put}", json=json_data
        )
        code_response = response.get_json()[self.response_key]
        assert (
            code_response == self.expect_status_put
        ), f"Expected {self.expect_status_put} got {code_response}"
