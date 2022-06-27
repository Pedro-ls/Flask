import os

from dotenv import load_dotenv

env = load_dotenv(".env")


class ConfigGlobal:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(ConfigGlobal):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.realpath("tmp/bd.db")
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = "development"


class ProdConfig(ConfigGlobal):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.realpath("tmp/bd.db")
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = "development"


config = {
    "development": DevConfig,
    "production": ProdConfig
}
