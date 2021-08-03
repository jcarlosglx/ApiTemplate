from typing import Dict
from string import ascii_uppercase, digits
from dataclasses import dataclass
from datetime import datetime
from random import randint, random, choices


def get_dummy_json_test(data_class: dataclass) -> Dict:
    data_json = {}
    dict_variables: Dict = data_class.__annotations__
    for key in dict_variables.keys():
        type_field = str(dict_variables[key])
        name_field = str(key)
        if type_field == "<class 'int'>":
            data_json[name_field] = randint(1, 10)
        if type_field == "<class 'float'>":
            data_json[name_field] = random()
        if type_field == "<class 'bool'>":
            data_json[name_field] = random() >= 0.5
        if type_field == "<class 'str'>":
            data_json[name_field] = "".join(choices(ascii_uppercase + digits, k=10))
        if type_field == "<class 'datetime'>":
            data_json[name_field] = datetime.now()
        else:
            print(f"Not define values for {name_field} type {type_field}")
    return data_json
