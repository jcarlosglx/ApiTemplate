from flask_sqlalchemy import SQLAlchemy as BaseSQLAlchemy


class CustomSQLAlchemy(BaseSQLAlchemy):
    def apply_pool_defaults(self, app, options):
        options = super().apply_pool_defaults(app, options)
        options["pool_pre_ping"] = True
        return options


def load_models():
    from app.models.childrenModel import ChildrenModel
    from app.models.fatherModel import FatherModel
    from app.models.logModel import LogModel


db = CustomSQLAlchemy()
