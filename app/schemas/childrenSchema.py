from marshmallow import Schema


class ChildrenSchema(Schema):
    name: str
    age: int
    father_id: int
