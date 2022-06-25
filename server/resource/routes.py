from flask import Blueprint

from server.resource.user_route import router_users

# Todas as roteadores que
# criar deve ser importando
# dentro deste array


routes: list[Blueprint] = [
    router_users
]
