from datetime import datetime
from sqlalchemy import DateTime, Integer, Float, String, Boolean


def get_dummy_record(n: int, some_class):
    new_record = some_class()
    for key in some_class.__table__.columns.keys():
        type_column = some_class.__table__.columns[key].type
        if isinstance(type_column, Integer) and key != "id":
            setattr(new_record, key, n)
        elif isinstance(type_column, Float):
            setattr(new_record, key, float(f"{n}.{n}"))
        elif isinstance(type_column, String):
            setattr(new_record, key, f"{n}")
        elif isinstance(type_column, Boolean):
            setattr(new_record, key, True)
        elif isinstance(type_column, DateTime):
            setattr(new_record, key, datetime.now())
        else:
            if key != "id":
                print(f"Enable to set a default value for {type_column}")
    return new_record
