from test.base_test.baseTest import BasePutTest
from test.config.configTest import ConfigTest

from app.messages.statusMessages import STATUS_405
from app.schemas.fatherSchema import FatherSchema


class TestMiddleware(BasePutTest):
    endpoint_put = ConfigTest.endpoint_father
    schema_put = FatherSchema
    expect_status_put = STATUS_405
