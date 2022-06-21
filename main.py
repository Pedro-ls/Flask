# importa o flask
from flask import Flask
# importa o ORM para usar o banco de dados
from flask_sqlalchemy import SQLAlchemy
# Chama a classe estática que guarda
# as instâncias do app e do baanco de dados
from server import Server

# inicia instancia do Flask
# __name__ é uma variavel que identifica o modulo
app = Flask(__name__)

# esse arquivo chama o arquivo config.py que está na raiz do projeto
# ele é usado para passar configurações para o app Flask
app.config.from_object("config")
# cria uma variavel de conexão
database = SQLAlchemy(app)

# guarda a instancia do app
Server.app = app

# guarda a instancia do Banco de dados
Server.db = database

# importa os arquivos resource/__init__.py
# arquivos serve para mapiar rotas
from resource import *
# importa os arquivos entities/__init__.py
# arquivo serve para criar entidades do banco dados
from entities import *