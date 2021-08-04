from requests import get, post, patch, delete, put
from typing import Type
from marshmallow import Schema
from app.messages.statusMessages import STATUS_200
from test.helpers.dummy_json_test.dummy_json_test import get_dummy_json_test
from test.config.configTest import ConfigTest


class BaseGetTest:
    expect_status_get: str = STATUS_200
    url_get: str = ConfigTest.URL
    endpoint_get: str
    response_key: str = ConfigTest.response_key

    def test_get(self):
        response = get(f"{self.url_get}{self.endpoint_get}")
        assert response.json()[self.response_key] == self.expect_status_get


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
