from test.base_test.baseTest import BaseGetIndividualTest, BasePatchTest, BaseDeleteTest, BasePostTest
from app.messages.statusMessages import STATUS_500
from test.config.configTest import ConfigTest
from app.schemas.childrenSchema import ChildrenSchema
from app.schemas.fatherSchema import FatherSchema


class TestWrongDataChildren(BaseGetIndividualTest, BasePatchTest, BaseDeleteTest, BasePostTest):
    expect_status_get = STATUS_500
    expect_status_delete = STATUS_500
    expect_status_post = STATUS_500
    expect_status_patch = STATUS_500

    id_get = 1000
    id_patch = 1000
    id_delete = 1000

    endpoint_get = ConfigTest.endpoint_children
    endpoint_post = ConfigTest.endpoint_children
    endpoint_patch = ConfigTest.endpoint_children
    endpoint_delete = ConfigTest.endpoint_children

    schema_post = FatherSchema
    schema_patch = FatherSchema


class TestWrongDataFather(BaseGetIndividualTest, BasePatchTest, BaseDeleteTest, BasePostTest):
    expect_status_post = STATUS_500
    expect_status_get = STATUS_500
    expect_status_delete = STATUS_500
    expect_status_patch = STATUS_500

    id_get = 1000
    id_patch = 1000
    id_delete = 1000

    endpoint_get = ConfigTest.endpoint_father
    endpoint_patch = ConfigTest.endpoint_father
    endpoint_delete = ConfigTest.endpoint_father
    endpoint_post = ConfigTest.endpoint_father

    schema_patch = ChildrenSchema
    schema_post = ChildrenSchema
