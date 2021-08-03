from marshmallow import Schema, fields


class FatherSchema(Schema):
    age: int = fields.Integer()
    name: str = fields.String()
