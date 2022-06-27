from flask import Flask

import os
# importa os, que é uma lib para conseguir
# acessar algumas coisas do sistema operacional

# importações para Banco de dados
# importa as entities
import server.entities
import server.entities as database
from flask_migrate import Migrate

# importa as schemas de serializers
import server.schemas_serializable
import server.schemas_serializable as serializer

# importa as rotas e o registrador de rotas
from server.resource.routes import routes
from server.resource import registerRoutes


# factory que inicia o projeto
def create_app(config=None):
    """
    :param config: instancia classe de configuração
    :return Flask(): instância de um app Flask
    """
    app: Flask = Flask(__name__)  # cria instancia

    app.config.from_object(config)  # passa configuração para o app

    if config is None:
        con = "sqlite:///" + os.path.realpath("tmp/bd.db")  # paga path absoluta e junta com tmp/bd
        app.config['SQLALCHEMY_DATABASE_URI'] = con

        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    database.init_database(app)  # inicia SQLAlchemy
    Migrate(app, app.db)  # inicia o classe de migração

    serializer.init_series(app)  # inicia serializers
    registerRoutes(app, routes)  # registra a rotas do array dentro do array de routes.py

    return app  # retorna uma instância da classe Flask configurada
