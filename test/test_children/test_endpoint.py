from test.base_test.baseTest import (
    BasePatchTest,
    BaseDeleteTest,
    BaseGetGeneralTest,
    BasePostTest,
    BaseGetIndividualTest
)
from test.config.configTest import ConfigTest
from app.schemas.childrenSchema import ChildrenSchema


class TestChildren(BaseGetGeneralTest, BasePostTest, BasePatchTest, BaseDeleteTest, BaseGetIndividualTest):
    endpoint_post = ConfigTest.endpoint_children
    endpoint_get = ConfigTest.endpoint_children
    endpoint_patch = ConfigTest.endpoint_children
    endpoint_delete = ConfigTest.endpoint_children

    schema_post = ChildrenSchema
    schema_patch = ChildrenSchema
