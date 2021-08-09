from test.base_test.baseTest import BaseGetGeneralTest
from test.config.configTest import ConfigTest


class TestHealthCheck(BaseGetGeneralTest):
    endpoint_get = ConfigTest.endpoint_health_check_server