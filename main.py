import os

from server import create_app
from config import config

if __name__ == "__main__":
    appServer = create_app(
        config=config["development"]
    )

    appServer.run(debug=True)
