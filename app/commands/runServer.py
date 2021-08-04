from app.commands.baseCommand import BaseCommand
from app.routes.blueprints import load_blueprints
from app.entryApp import (
    get_config_server,
    check_connection_db,
)


class RunServer(BaseCommand):

    NAME: str = "run_server"

    def run(self):
        config = get_config_server()
        load_blueprints(self.instance)
        is_alive_db = check_connection_db()
        if is_alive_db:
            self.instance.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
        else:
            print("Unable to connect with the database")
