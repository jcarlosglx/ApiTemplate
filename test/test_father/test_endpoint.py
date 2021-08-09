from test.base_test.baseTest import (BaseDeleteTest, BaseGetGeneralTest,
                                     BaseGetIndividualTest, BasePatchTest,
                                     BasePostTest)
from test.config.configTest import ConfigTest

from app.schemas.fatherSchema import FatherSchema


class TestFather(
    BaseGetGeneralTest,
    BasePostTest,
    BaseDeleteTest,
    BasePatchTest,
    BaseGetIndividualTest,
):
    endpoint_get = ConfigTest.endpoint_father
    endpoint_patch = ConfigTest.endpoint_father
    endpoint_post = ConfigTest.endpoint_father
    endpoint_delete = ConfigTest.endpoint_father

    schema_post = FatherSchema
    schema_patch = FatherSchema
