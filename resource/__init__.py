from server import Server


@Server.app.route("/test")
def test():
    return "test"