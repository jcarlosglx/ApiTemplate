from app.models import db
from app.helpers.records.createRecords import create_records
from app import create_app, get_config_app, get_config_server, check_connection_db
from flask_script import Manager
from app.routes.blueprints import load_blueprints
from app.models import load_models
from app.services.healthCheckServer import HealthCheckServer


type_config_app = get_config_app()
instance = create_app()
manager_commands = Manager(instance)
scheduler = HealthCheckServer(instance)


@manager_commands.command
def run_server():
    config = get_config_server()
    load_blueprints(instance)
    is_alive_db = check_connection_db()
    if is_alive_db:
        instance.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
    else:
        print("Unable to connect with the database")


@manager_commands.command
def init_db():
    load_models()
    db.create_all()


@manager_commands.command
def create_data():
    is_alive_db = check_connection_db()
    if is_alive_db:
        init_db()
        create_records(10)
    else:
        print("Unable to connect with the database")


if __name__ == "__main__":
    manager_commands.run()

if __name__ == "main":
    with instance.test_request_context():
        load_blueprints(instance)
