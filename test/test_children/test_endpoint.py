from test.base_test.baseTest import BasePatchTest, BaseDeleteTest, BaseGetTest, BasePostTest
from test.config.configTest import ConfigTest
from app.schemas.childrenSchema import ChildrenSchema


class TestChildren(BaseGetTest, BasePostTest, BaseDeleteTest, BasePatchTest):
    endpoint_get = ConfigTest.endpoint_children
    endpoint_patch = ConfigTest.endpoint_children
    endpoint_post = ConfigTest.endpoint_children
    endpoint_delete = ConfigTest.endpoint_children

    schema_post = ChildrenSchema
    schema_patch = ChildrenSchema
