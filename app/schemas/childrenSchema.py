from dataclasses import dataclass
from marshmallow_dataclass import class_schema


@dataclass
class ChildrenDataClass:
    identifier: int
    name: str
    age: int
    father_id: int


ChildrenSchema = class_schema(ChildrenDataClass)
