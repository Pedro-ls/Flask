# como se cria uma rota
from flask import Blueprint

# instancia uma blueprint que é um modelo de roteamento
router_users = Blueprint("user", __name__)


# cria rotas
@router_users.route("/users")
def users():
    return "users"
