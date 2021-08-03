from marshmallow import Schema, fields


class ChildrenSchema(Schema):
    name: str = fields.String()
    age: int = fields.Integer()
    father_id: int = fields.Integer()
