from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_database(app: Flask):
    """
    :description: Inicia variavel db
    :param app: Instância do Flask
    """
    db.init_app(app)
    app.db = db


# Aqui vai as entidades
# Examplo de entidade ou modelo
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
