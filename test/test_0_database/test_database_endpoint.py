from test.base_test.baseTest import BaseGetTest
from test.config.configTest import ConfigTest


class TestDeleteDB(BaseGetTest):
    endpoint_get = ConfigTest.endpoint_database_delete


class TestCreateDB(BaseGetTest):
    endpoint_get = ConfigTest.endpoint_database_create
