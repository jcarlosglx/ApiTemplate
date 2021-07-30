from app.models import db
from app.helpers.records.createRecords import create_records
from app import create_app
from os import environ
from flask_script import Manager
from app.routes.blueprints import load_blueprints
from app.models import load_models
from app.services.healthCheckServer import HealthCheckServer


def check_connection_db() -> bool:
    try:
        db.session.execute("SELECT 1")
        return True
    except Exception as error:
        return False


def get_configuration() -> str:
    type_configuration = "DEV"
    if environ.get("PATH_DB"):
        type_configuration = "DEPLOY"
    return type_configuration


type_config = get_configuration()
instance = create_app(type_config)
manager_commands = Manager(instance)
scheduler = HealthCheckServer(instance, sec=120)


@manager_commands.command
def run_server(debug=False):
    load_blueprints(instance)
    is_alive_db = check_connection_db()
    if is_alive_db:
        instance.run(debug=debug)
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
