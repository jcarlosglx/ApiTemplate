from marshmallow import Schema, fields


class FatherSchema(Schema):
    name = fields.String()
    age = fields.Integer()
