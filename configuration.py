class ConfigGlobal:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(ConfigGlobal):
    SQLALCHEMY_DATABASE_URI = "sqlite:////bd.db"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = "development"


class ProdConfig(ConfigGlobal):
    pass


config = {
    "development": DevConfig,
    "production": ProdConfig
}
