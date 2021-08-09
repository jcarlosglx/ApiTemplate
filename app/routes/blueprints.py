from flask import Flask


def load_blueprints(instance: Flask):
    from app.routes.childrenRoute import children_blueprint
    from app.routes.databaseRoute import database_blueprint
    from app.routes.fatherRoute import father_blueprint
    from app.routes.healthCheckServerRoute import health_check_server_blueprint

    prefix = instance.config["APPLICATION_ROOT"]

    instance.register_blueprint(father_blueprint, url_prefix=prefix)
    instance.register_blueprint(database_blueprint, url_prefix=prefix)
    instance.register_blueprint(children_blueprint, url_prefix=prefix)
    instance.register_blueprint(health_check_server_blueprint, url_prefix=prefix)
