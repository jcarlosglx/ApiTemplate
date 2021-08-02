from datetime import datetime
from sqlalchemy import DateTime, Integer, Float, String, Boolean
from app.models.entryORM import db


def get_dummy_record(n: int, class_model: db.Model) -> db.Model:
    new_record = class_model()
    for key in class_model.__table__.columns.keys():
        type_column = class_model.__table__.columns[key].type
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
