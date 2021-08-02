from dataclasses import dataclass
from marshmallow_dataclass import class_schema


@dataclass
class FatherDataClass:
    age: int
    identifier: int
    name: str


FatherSchema = class_schema(FatherDataClass)
