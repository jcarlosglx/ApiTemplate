from flask import Flask


def load_blueprints(instance: Flask):
    from app.routes.fatherRoute import father_blueprint
    from app.routes.childrenRoute import children_blueprint

    prefix = instance.config["APPLICATION_ROOT"]

    instance.register_blueprint(father_blueprint)
    instance.register_blueprint(children_blueprint)
