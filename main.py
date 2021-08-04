from app.models.entryORM import db
from app.helpers.records.createRecords import create_records
from app.helpers.records.deleteRecords import delete_records
from app.entryApp import (
    create_app,
    get_config_app,
    get_config_server,
    get_config_db,
    check_connection_db,
)
from flask_script import Manager
from os import system as system_command
from app.routes.blueprints import load_blueprints
from app.models.entryORM import load_models
from app.services.healthCheckServer import HealthCheckServer
from app.services.testServer import TestServer

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
def run_tests():
    is_alive_db = check_connection_db()
    if is_alive_db:
        config = get_config_server()
        with TestServer(config.TIME_WAKE_SEC) as test_server:
            delete_data()
            create_data()
            test_files_path = test_server.test_files_path
            system_command(f"coverage run -m pytest {test_files_path}")
            system_command("coverage html")
            system_command("coverage report")
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
        config = get_config_db()
        create_records(config.N_DUMMY_RECORDS)
    else:
        print("Unable to connect with the database")


@manager_commands.command
def delete_data():
    is_alive_db = check_connection_db()
    if is_alive_db:
        delete_records()
    else:
        print("Unable to connect with the database")


if __name__ == "__main__":
    manager_commands.run()


if __name__ == "main":
    with instance.test_request_context():
        load_blueprints(instance)
