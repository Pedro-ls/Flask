from flask_marshmallow import Marshmallow

# faz um 'serialize' nos dados
# ou melhor converte para JSON
# Pode validar dados
from server.entities import User

ma: Marshmallow = Marshmallow()  # instância de marshmallow


def init_series(app):  # def que inicia classe marshmallow
    ma.init_app(app)  # inicia app server
    app.ma = ma  # cria atributo dentro do server que poderá ser acessado posterior mente


# Criar os Serializers aqui

class UserSchema(ma.Schema):  # modelo de serializer
    class Meta:
        model = User
