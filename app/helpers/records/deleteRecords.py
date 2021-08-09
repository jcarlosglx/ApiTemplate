from typing import NoReturn

from app.models.entryORM import db


def delete_records() -> NoReturn:
    db.drop_all()
    # Code for postgresql
    # for table in db.metadata.tables.keys():
    #     db.session.execute(f"TRUNCATE TABLE {table} CASCADE")
    #     db.session.execute(f"ALTER SEQUENCE {table}_id_seq RESTART WITH 1")
    # db.session.commit()
