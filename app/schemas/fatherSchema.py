from marshmallow import Schema, fields


class BaseSchema(Schema):
    name = fields.String()
    age = fields.Integer()