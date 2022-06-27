# como se cria uma rota
from flask import Blueprint

# instancia uma blueprint que é um modelo de roteamento
from server.entities import db, User

router_users = Blueprint("user", __name__)


# cria rotas
@router_users.route("/users")
def users():
    user = User()
    user.username = "pedro"
    user.email = "pedro@gmail.com"
    user.password = "jdsfjdsfods"
    db.session.add(user)
    db.commit()
    return "users teste"