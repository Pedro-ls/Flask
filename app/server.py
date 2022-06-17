from flask import Flask
class App:
    def __init__(self, controllers=None, config=None, debug = True):
        self.controllers = controllers
        self.config = config
        self.server = Flask(self.config)
        self.debug = debug
    def config(self, config=None):
        self.config = config

    def controllers(self, controllers=None):
        self.controllers = controllers

    def run(self):
        return self.server.run(debug=self.debug)

