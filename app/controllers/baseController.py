from flask import request


class BaseController:
    model = None
    data_json = request.get_json()
    schema = None
    rules = None