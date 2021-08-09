from test.base_test.baseTest import BasePutTest, BaseGetGeneralTest
from test.config.configTest import ConfigTest

from app.messages.statusMessages import STATUS_405, STATUS_500
from app.schemas.fatherSchema import FatherSchema


class TestMiddleware(BasePutTest, BaseGetGeneralTest):
    endpoint_put = ConfigTest.endpoint_father
    endpoint_get = "ThisEndpointShouldNotExist"
    schema_put = FatherSchema
    expect_status_get = STATUS_500
    expect_status_put = STATUS_405
