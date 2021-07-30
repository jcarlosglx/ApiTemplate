from marshmallow import Schema, fields


class ChildrenSchema(Schema):
    name = fields.String()
    age = fields.Integer()
    parent_id = fields.Integer()
