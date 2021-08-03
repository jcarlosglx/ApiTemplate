from test.base_test.baseTest import BaseGetTest
from test.config.configTest import ConfigTest


class TestChildren(BaseGetTest):
    endpoint_get = ConfigTest.endpoint_children
