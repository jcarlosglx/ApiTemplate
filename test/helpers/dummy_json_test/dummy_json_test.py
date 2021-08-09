from datetime import datetime
from random import choices, randint, random
from string import ascii_uppercase, digits
from typing import Dict, Type

from marshmallow import Schema


def get_dummy_json_test(schema: Type[Schema]) -> Dict:
    data_json = {}
    dict_variables: Dict = schema.__annotations__
    for key in dict_variables.keys():
        type_field = str(dict_variables[key])
        name_field = str(key)
        if type_field == "<class 'int'>":
            data_json[name_field] = randint(1, 10)
        elif type_field == "<class 'float'>":
            data_json[name_field] = random()
        elif type_field == "<class 'bool'>":
            data_json[name_field] = random() >= 0.5
        elif type_field == "<class 'str'>":
            data_json[name_field] = "".join(choices(ascii_uppercase + digits, k=10))
        elif type_field == "<class 'datetime'>":
            data_json[name_field] = datetime.now()
        else:
            print(isinstance(type_field, int))
    return data_json
