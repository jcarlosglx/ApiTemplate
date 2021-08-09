from app.commands.baseCommand import BaseCommand
from app.entryApp import check_connection_db
from app.helpers.records.deleteRecords import delete_records


class DeleteData(BaseCommand):

    NAME: str = "delete_data"

    def run(self):
        is_alive_db = check_connection_db()
        if is_alive_db:
            delete_records()
        else:
            print("Unable to connect with the database")
