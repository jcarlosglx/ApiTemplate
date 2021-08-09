from app.commands.baseCommand import BaseCommand
from app.entryApp import check_connection_db, get_config_db
from app.helpers.records.createRecords import create_records
from app.models.entryORM import db, load_models


class CreateData(BaseCommand):

    NAME: str = "create_data"

    def run(self):
        is_alive_db = check_connection_db()
        if is_alive_db:
            load_models()
            db.create_all()
            config = get_config_db()
            create_records(config.N_DUMMY_RECORDS)
        else:
            print("Unable to connect with the database")
