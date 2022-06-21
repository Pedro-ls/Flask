from flask import Flask
from flask_sqlalchemy import SQLAlchemy




class Server:
    app: Flask = None
    db: SQLAlchemy = None

    @classmethod
    def init(cls):
        pass

