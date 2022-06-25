from flask import Blueprint


# aqui você pode criar suas "libs" extra

# registra rotas (não mexer)
def registerRoutes(server, routes: list[Blueprint]):
    for route in routes:
        server.register_blueprint(route)


class HttpCode:
    """
        :description:
        HttpCode Aqui pode se cadastrar os HttpCode
        Dentro da variavel __code__
        Você usa da seguinte forma
        HttpCode.getCode(200).code --> str
    """
    __code__ = {
        200: "Ok",
        400: "Not Found",
        500: "Error Server"
    }

    def __init__(self, code):
        self.code = code

    @classmethod
    def getCode(cls, number: int):
        """
        Setar o código Http que quer na requisição
        :param number: codigo http
        :return: HttpCode
        :attributes: code
        """
        return cls(cls.__code__[number])
