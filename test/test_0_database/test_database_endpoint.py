from test.base_test.baseTest import BaseGetGeneralTest
from test.config.configTest import ConfigTest


class TestDeleteDB(BaseGetGeneralTest):
    endpoint_get = ConfigTest.endpoint_database_delete


class TestCreateDB(BaseGetGeneralTest):
    endpoint_get = ConfigTest.endpoint_database_create
