from typing import NoReturn

from app.helpers.records.dummyRecords import get_dummy_record
from app.models.childrenModel import ChildrenModel
from app.models.entryORM import db
from app.models.fatherModel import FatherModel
from app.models.logModel import LogModel


def create_records(size: int) -> NoReturn:
    for n in range(1, size + 1):
        new_log = get_dummy_record(n, LogModel)
        db.session.add(new_log)
        db.session.commit()

        new_father = get_dummy_record(n, FatherModel)
        db.session.add(new_father)
        db.session.commit()

        new_children = get_dummy_record(n, ChildrenModel)
        db.session.add(new_children)
        db.session.commit()
