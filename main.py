from app.commands.runServer import RunServer
from app.commands.initDB import InitDB
from app.commands.runTests import RunTests
from app.commands.deleteData import DeleteData
from app.commands.createData import CreateData
from app.entryApp import create_app, get_config_app
from flask_script import Manager
from app.routes.blueprints import load_blueprints
from app.services.healthCheckServer import HealthCheckServer

type_config_app = get_config_app()
instance = create_app()
manager_commands = Manager(instance)
manager_commands.add_command(RunTests.NAME, RunTests(instance))
manager_commands.add_command(RunServer.NAME, RunServer(instance))
manager_commands.add_command(InitDB.NAME, InitDB(instance))
manager_commands.add_command(DeleteData.NAME, DeleteData(instance))
manager_commands.add_command(CreateData.NAME, CreateData(instance))
scheduler = HealthCheckServer(instance)


if __name__ == "__main__":
    manager_commands.run()


if __name__ == "main":
    with instance.test_request_context():
        load_blueprints(instance)
