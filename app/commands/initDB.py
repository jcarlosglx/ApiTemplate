from app.commands.baseCommand import BaseCommand
from app.models.entryORM import db, load_models


class InitDB(BaseCommand):

    NAME: str = "init_db"

    def run(self):
        load_models()
        db.create_all()
