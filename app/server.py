from flask import Flask

from app.models.user import User


class App:


    def __init__(self, debug = True):
        self.controllers = None
        self.config = None
        self.server = Flask(__name__)
        self.debug = debug
        self.models = [
            User
        ]


    def config(self, config=None):
        self.config = config


    def controllers(self, controllers=None):
        self.controllers = controllers


    def run(self):
        return self.server.run(debug=self.debug)

