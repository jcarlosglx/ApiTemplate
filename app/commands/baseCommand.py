from flask import Flask
from flask_script import Command


class BaseCommand(Command):

    NAME: str

    def __init__(self, instance: Flask):
        Command.__init__(self)
        self.instance = instance

    def run(self):
        pass
