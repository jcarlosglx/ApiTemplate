from os import system as system_command

from app.commands.baseCommand import BaseCommand
from app.entryApp import check_connection_db, get_config_db, get_config_server
from app.helpers.records.createRecords import create_records
from app.helpers.records.deleteRecords import delete_records
from app.models.entryORM import db, load_models
from app.services.testServer import TestServer


class RunTests(BaseCommand):

    NAME: str = "run_tests"

    def run(self):
        is_alive_db = check_connection_db()
        if is_alive_db:
            config = get_config_server()
            with TestServer(config.TIME_WAKE_SEC) as test_server:
                delete_records()

                load_models()
                db.create_all()
                config = get_config_db()
                create_records(config.N_DUMMY_RECORDS)

                test_files_path = test_server.test_files_path
                system_command(f"coverage run -m pytest {test_files_path}")
                system_command("coverage html")
                system_command("coverage report")
        else:
            print("Unable to connect with the database")
